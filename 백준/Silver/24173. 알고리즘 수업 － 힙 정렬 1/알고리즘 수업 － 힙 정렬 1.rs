use std::io::{self};

static mut CHANGES: Vec<(i32, i32)> = Vec::new();

fn heap_sort(a: &mut Vec<i32>, n: usize) {
    unsafe {
        build_min_heap(a, n);
        for i in (2..=n).rev() {
            a.swap(1, i);
            let (smaller, larger) = (a[1].min(a[i]), a[1].max(a[i]));
            CHANGES.push((smaller, larger));
            heapify(a, 1, i - 1);
        }
    }
}

fn build_min_heap(a: &mut Vec<i32>, n: usize) {
    for i in (1..=n/2).rev() {
        heapify(a, i, n);
    }
}

fn heapify(a: &mut Vec<i32>, k: usize, n: usize) {
    unsafe {
        let left = 2 * k;
        let right = 2 * k + 1;
        if right <= n {
            let smaller = if a[left] < a[right] { left } else { right };
            if a[smaller] < a[k] {
                a.swap(smaller, k);
                let (smaller2, larger) = (a[smaller].min(a[k]), a[smaller].max(a[k]));
                CHANGES.push((smaller2, larger));
                heapify(a, smaller, n);
            }
        } else if left <= n && a[left] < a[k] {
            a.swap(left, k);
            let (smaller2, larger) = (a[left].min(a[k]), a[left].max(a[k]));
            CHANGES.push((smaller2, larger));
            heapify(a, left, n);
        }
    }
}

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    input.clear();
    let mut a: Vec<i32> = vec![0];
    io::stdin().read_line(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    for _ in 0..n {
        let num: i32 = tokens.next().unwrap().parse().unwrap();
        a.push(num);
    }
    heap_sort(&mut a, n);
    let answer = if k >= unsafe { CHANGES.len() } {
        "-1".to_string()
    } else {
        format!("{} {}", unsafe { CHANGES[k - 1].0 }, unsafe { CHANGES[k - 1].1 })
    };
    println!("{}", answer);
}
