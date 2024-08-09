use std::io::{self, Read, Write};
use std::cmp::min;
use std::f64::consts::PI;

const MOD: i64 = 1_000_000_007;

#[derive(Clone, Copy)]
#[derive(PartialEq)]
struct LazyMultiplier {
    a: i64,
    b: i64,
}

impl LazyMultiplier {
    fn new(a: i64, b: i64) -> LazyMultiplier {
        LazyMultiplier { a, b }
    }

    fn __eq__(self, other:LazyMultiplier) -> bool {
        return self.a==other.a && self.b==other.b
    }
}

struct SegmentTree {
    size: usize,
    default_value: i64,
    no_update_value: LazyMultiplier,
    tree_height: usize,
    tree_size: usize,
    base_index: usize,
    tree: Vec<i64>,
    lazy: Vec<LazyMultiplier>,
    lazy_multiplier: Vec<i64>,
    index_offset: usize,
}

impl SegmentTree {
    fn new(initial_values: Vec<i64>, default_value: i64, base_index: usize) -> SegmentTree {
        let size = initial_values.len();
        let tree_height = (size as f64).log2().ceil() as usize;
        let tree_size = 1 << tree_height;
        let mut tree = vec![default_value; 2 * tree_size];
        let lazy = vec![LazyMultiplier::new(1, 0); 2 * tree_size];
        let lazy_multiplier = vec![0; 2 * tree_size];
        let index_offset = tree_size - base_index;
        let mut segment_tree = SegmentTree {
            size,
            default_value,
            no_update_value: LazyMultiplier::new(1, 0),
            tree_height,
            tree_size,
            base_index,
            tree,
            lazy,
            lazy_multiplier,
            index_offset,
        };
        segment_tree.build_tree(&initial_values);
        segment_tree
    }

    fn update_point(&mut self, index: usize, value: LazyMultiplier, opcode: &str) {
        let mut index = index + self.index_offset;
        for level in (1..=self.tree_height).rev() {
            self.propagate_update(index >> level);
        }
        match opcode {
            "add" => self.apply_update_add(index, value),
            "mul" => self.apply_update_mul(index, value),
            "set" => self.apply_update_set(index, value),
            _ => (),
        }
        for level in 1..=self.tree_height {
            self.merge_children(index >> level);
        }
    }

    fn update_range(&mut self, left: usize, right: usize, value: LazyMultiplier, opcode: &str) {
        let mut left = left + self.index_offset;
        let mut right = right + self.index_offset;
        for level in (1..=self.tree_height).rev() {
            if (left >> level) << level != left {
                self.propagate_update(left >> level);
            }
            if ((right + 1) >> level) << level != right + 1 {
                self.propagate_update(right >> level);
            }
        }
        let (mut L, mut R) = (left, right);
        while L <= R {
            if L % 2 == 1 {
                match opcode {
                    "add" => self.apply_update_add(L, value),
                    "mul" => self.apply_update_mul(L, value),
                    "set" => self.apply_update_set(L, value),
                    _ => (),
                }
                L += 1;
            }
            if R % 2 == 0 {
                match opcode {
                    "add" => self.apply_update_add(R, value),
                    "mul" => self.apply_update_mul(R, value),
                    "set" => self.apply_update_set(R, value),
                    _ => (),
                }
                R -= 1;
            }
            L >>= 1;
            R >>= 1;
        }
        for level in 1..=self.tree_height {
            if (left >> level) << level != left {
                self.merge_children(left >> level);
            }
            if ((right + 1) >> level) << level != right + 1 {
                self.merge_children(right >> level);
            }
        }
    }

    fn query_point(&mut self, index: usize) -> i64 {
        let mut index = index + self.index_offset;
        for level in (1..=self.tree_height).rev() {
            self.propagate_update(index >> level);
        }
        self.tree[index]
    }

    fn query_range(&mut self, left: usize, right: usize) -> i64 {
        let (mut left_result, mut right_result) = (self.default_value, self.default_value);
        let (mut left, mut right) = (left + self.index_offset, right + self.index_offset);
        for level in (1..=self.tree_height).rev() {
            if (left >> level) << level != left {
                self.propagate_update(left >> level);
            }
            if ((right + 1) >> level) << level != right + 1 {
                self.propagate_update(right >> level);
            }
        }
        while left <= right {
            if left % 2 == 1 {
                left_result = self.combine_node_values(left_result, self.tree[left]);
                left += 1;
            }
            if right % 2 == 0 {
                right_result = self.combine_node_values(self.tree[right], right_result);
                right -= 1;
            }
            left >>= 1;
            right >>= 1;
        }
        self.combine_node_values(left_result, right_result)
    }

    fn build_tree(&mut self, initial_values: &Vec<i64>) {
        for (i, &v) in initial_values.iter().enumerate() {
            self.tree[i + self.tree_size] = v;
            self.lazy[i + self.tree_size] = LazyMultiplier::new(1, 0);
            self.lazy_multiplier[i + self.tree_size] = 1;
        }
        for i in (1..self.tree_size).rev() {
            self.merge_children(i);
        }
    }

    fn apply_update_add(&mut self, index: usize, value: LazyMultiplier) {
        self.tree[index] = self.apply_lazy_update_add(value, self.tree[index], self.lazy_multiplier[index]);
        if index < self.tree_size {
            self.lazy[index] = self.accumulate_lazy_updates_add(value, self.lazy[index]);
        }
    }

    fn apply_update_mul(&mut self, index: usize, value: LazyMultiplier) {
        self.tree[index] = self.apply_lazy_update_mul(value, self.tree[index], self.lazy_multiplier[index]);
        if index < self.tree_size {
            self.lazy[index] = self.accumulate_lazy_updates_mul(value, self.lazy[index]);
        }
    }

    fn apply_update_set(&mut self, index: usize, value: LazyMultiplier) {
        self.tree[index] = self.apply_lazy_update_set(value, self.tree[index], self.lazy_multiplier[index]);
        if index < self.tree_size {
            self.lazy[index] = self.accumulate_lazy_updates_set(value, self.lazy[index]);
        }
    }

    fn propagate_update(&mut self, index: usize) {
        self.apply_update_add(2 * index, self.lazy[index]);
        self.apply_update_add(2 * index + 1, self.lazy[index]);
        self.lazy[index] = self.no_update_value;
    }

    fn merge_children(&mut self, index: usize) {
        self.tree[index] = self.combine_node_values(self.tree[2 * index], self.tree[2 * index + 1]);
        self.lazy_multiplier[index] = self.lazy_multiplier[2 * index] + self.lazy_multiplier[2 * index + 1];
    }

    fn combine_node_values(&self, left: i64, right: i64) -> i64 {
        (left + right) % MOD
    }

    fn apply_lazy_update_add(&self, lazy_value: LazyMultiplier, node_value: i64, lazy_multiplier: i64) -> i64 {
        (lazy_value.a * node_value % MOD + lazy_multiplier * lazy_value.b % MOD) % MOD
    }

    fn apply_lazy_update_mul(&self, lazy_value: LazyMultiplier, node_value: i64, lazy_multiplier: i64) -> i64 {
        (lazy_value.a * node_value % MOD + lazy_multiplier * lazy_value.b % MOD) % MOD
    }

    fn apply_lazy_update_set(&self, lazy_value: LazyMultiplier, node_value: i64, lazy_multiplier: i64) -> i64 {
        if lazy_value == self.no_update_value {
            node_value
        } else {
            lazy_value.b * lazy_multiplier % MOD
        }
    }

    fn accumulate_lazy_updates_add(&self, lazy_value1: LazyMultiplier, lazy_value2: LazyMultiplier) -> LazyMultiplier {
        LazyMultiplier::new(lazy_value1.a * lazy_value2.a % MOD, (lazy_value1.b + lazy_value2.b * lazy_value1.a) % MOD)
    }

    fn accumulate_lazy_updates_mul(&self, lazy_value1: LazyMultiplier, lazy_value2: LazyMultiplier) -> LazyMultiplier {
        LazyMultiplier::new(lazy_value1.a * lazy_value2.a % MOD, (lazy_value1.b + lazy_value2.b * lazy_value1.a) % MOD)
    }

    fn accumulate_lazy_updates_set(&self, lazy_value1: LazyMultiplier, lazy_value2: LazyMultiplier) -> LazyMultiplier {
        LazyMultiplier::new(0, (lazy_value1.a * lazy_value2.a + lazy_value1.b) % MOD)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace().map(|s| s.parse::<i64>().unwrap());
    let n = tokens.next().unwrap() as usize;
    let numbers: Vec<i64> = (0..n).map(|_| tokens.next().unwrap()).collect();
    let m = tokens.next().unwrap() as usize;
    let mut segment_tree = SegmentTree::new(numbers, 0, 1);
    let mut answer = Vec::new();
    for _ in 0..m {
        let opcode = tokens.next().unwrap();
        match opcode {
            1 => {
                let x = tokens.next().unwrap() as usize;
                let y = tokens.next().unwrap() as usize;
                let v = tokens.next().unwrap();
                segment_tree.update_range(x, y, LazyMultiplier::new(1, v), "add");
            }
            2 => {
                let x = tokens.next().unwrap() as usize;
                let y = tokens.next().unwrap() as usize;
                let v = tokens.next().unwrap();
                segment_tree.update_range(x, y, LazyMultiplier::new(v, 0), "mul");
            }
            3 => {
                let x = tokens.next().unwrap() as usize;
                let y = tokens.next().unwrap() as usize;
                let v = tokens.next().unwrap();
                segment_tree.update_range(x, y, LazyMultiplier::new(0, v), "set");
            }
            4 => {
                let x = tokens.next().unwrap() as usize;
                let y = tokens.next().unwrap() as usize;
                answer.push(segment_tree.query_range(x, y).to_string());
            }
            _ => (),
        }
    }
    let output = answer.join("\n");
    io::stdout().write_all(output.as_bytes()).unwrap();
}
