use std::collections::{HashMap, VecDeque};
use std::io::{self, Read, Write};
use std::iter::Iterator;

// Constants
const INF: i64 = 10_i64.pow(18);
const MOD: i64 = 1_000_000_007;
const DELTA: [(i32, i32); 8] = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
];

// Utility function to check if coordinates are within bounds
fn is_inbound(pos_x: i32, pos_y: i32, size_x: i32, size_y: i32) -> bool {
    pos_x >= 0 && pos_x < size_x && pos_y >= 0 && pos_y < size_y
}

pub(crate) fn main() {
    // Reading input
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();

    // Lambda function to get the next input token as an integer
    let mut next_int = || -> i32 {
        tokens.next().unwrap().parse().unwrap()
    };

    let mut answers = Vec::new();
    let t = 1;  // You can adjust this as needed

    for _ in 0..t {
        let n = next_int();
        let m = next_int();
        let k = next_int();
        let mut food = vec![vec![5; n as usize]; n as usize];
        let mut delta_food = vec![vec![0; n as usize]; n as usize];
        for i in 0..n {
            for j in 0..n {
                delta_food[i as usize][j as usize] = next_int();
            }
        }

        let mut trees = vec![vec![HashMap::new(); n as usize]; n as usize];
        for _ in 0..m {
            let y = next_int() - 1;
            let x = next_int() - 1;
            let z = next_int();
            trees[y as usize][x as usize].entry(z).or_insert(1);
        }

        for a in 0..k {
            // Spring & Summer
            for r in 0..n {
                for c in 0..n {
                    if trees[r as usize][c as usize].is_empty() {
                        continue;
                    }

                    let mut new_trees = HashMap::new();
                    let mut dead_tree_age_sum = 0;
                    let mut current_food = food[r as usize][c as usize];

                    let mut keys: Vec<i32> = trees[r as usize][c as usize].keys().cloned().collect();
                    keys.sort();

                    for &age in keys.iter() {
                        let count = *trees[r as usize][c as usize].get(&age).unwrap();
                        let can_be_fed = current_food / age;
                        let fed_count = can_be_fed.min(count);

                        if fed_count < count {
                            dead_tree_age_sum += (age >> 1) * (count - fed_count);
                        }
                        if fed_count > 0 {
                            new_trees.insert(age + 1, fed_count);
                            current_food -= age * fed_count;
                        }
                    }
                    trees[r as usize][c as usize] = new_trees;
                    food[r as usize][c as usize] = current_food;
                    food[r as usize][c as usize] += dead_tree_age_sum;
                }
            }
            // Fall
            let mut trees_to_be_grown = vec![vec![0; n as usize]; n as usize];
            for r in 0..n {
                for c in 0..n {
                    for (&age, &count) in &trees[r as usize][c as usize] {
                        if age % 5 == 0 {
                            for &(dr, dc) in &DELTA {
                                let nr = r + dr;
                                let nc = c + dc;
                                if is_inbound(nr, nc, n, n) {
                                    trees_to_be_grown[nr as usize][nc as usize] += count;
                                }
                            }
                        }
                    }
                }
            }

            for r in 0..n {
                for c in 0..n {
                    let sapling_count = trees[r as usize][c as usize].get(&1).unwrap_or(&0) + trees_to_be_grown[r as usize][c as usize];
                    if sapling_count > 0 {
                        trees[r as usize][c as usize].insert(1, sapling_count);
                    }
                }
            }

            // Winter
            for r in 0..n {
                for c in 0..n {
                    food[r as usize][c as usize] += delta_food[r as usize][c as usize];
                }
            }
        }

        let answer: i32 = trees.iter()
            .map(|row| row.iter()
                .map(|cell| cell.values().sum::<i32>())
                .sum::<i32>())
            .sum();
        answers.push(answer);
    }

    for answer in answers {
        println!("{}", answer);
    }
}
