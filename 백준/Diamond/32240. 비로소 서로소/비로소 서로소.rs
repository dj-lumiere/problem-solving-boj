use std::collections::HashMap;
use std::io::{self, BufRead};
use std::cmp::min;
use std::collections::HashSet;

const MOD: i64 = 1_000_000_007;
const PRECOMPUTE_LIMIT: usize = 20_000_000;

fn precompute_mu_and_sums() -> (Vec<i64>, Vec<i64>) {
    let mut mu_i_small = vec![1; PRECOMPUTE_LIMIT + 1];
    let mut done_calculating = vec![false; PRECOMPUTE_LIMIT + 1];
    let mut sum_of_i_mu_i_small = vec![0; PRECOMPUTE_LIMIT + 1];

    for i in 2..=PRECOMPUTE_LIMIT {
        if !done_calculating[i] {
            for j in (i..=PRECOMPUTE_LIMIT).step_by(i) {
                mu_i_small[j] *= -1;
                done_calculating[j] = true;
            }
            for j in (i * i..=PRECOMPUTE_LIMIT).step_by(i * i) {
                mu_i_small[j] = 0;
            }
        }
    }

    for i in 1..=PRECOMPUTE_LIMIT {
        sum_of_i_mu_i_small[i] = (sum_of_i_mu_i_small[i - 1] + i as i64 * mu_i_small[i] % MOD) % MOD;
    }

    (mu_i_small, sum_of_i_mu_i_small)
}

fn sum_of_i_mu_i(x: i64, sum_of_i_mu_i_small: &Vec<i64>, sum_of_i_mu_i_big: &mut HashMap<i64, i64>) -> i64 {
    if x as usize <= PRECOMPUTE_LIMIT {
        return sum_of_i_mu_i_small[x as usize];
    }
    if let Some(&result) = sum_of_i_mu_i_big.get(&x) {
        return result;
    }

    let mut result = 1;
    let mut i = 2;
    while i <= x {
        let j = x / (x / i);
        //eprintln!("{i} {j}");
        result -= (((j as i128 * (j + 1) as i128 - i as i128 * (i - 1) as i128) / 2) % MOD as i128) as i64 * sum_of_i_mu_i(x / i, sum_of_i_mu_i_small, sum_of_i_mu_i_big) % MOD;
        result = (result + MOD) % MOD;
        i = j + 1;
    }

    sum_of_i_mu_i_big.insert(x, result);
    result
}

pub(crate) fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let n: i64 = input.parse().unwrap();

    let (mu_i_small, sum_of_i_mu_i_small) = precompute_mu_and_sums();
    let mut sum_of_i_mu_i_big = HashMap::new();

    let mut n_over_ds = Vec::new();
    for i in 1..=((n as f64).sqrt() as i64) {
        n_over_ds.push(i);
        n_over_ds.push(n / i);
    }

    n_over_ds.sort();
    n_over_ds.dedup();

    let mut lower_bound = Vec::new();
    let mut upper_bound = Vec::new();
    for i in 0..n_over_ds.len() - 1 {
        lower_bound.push(n_over_ds[i] + 1);
        upper_bound.push(n_over_ds[i + 1]);
    }

    lower_bound.reverse();
    upper_bound.reverse();
    lower_bound.push(1);
    upper_bound.push(1);

    let mut sum_of_i_mu_i_lower_bound = Vec::new();
    let mut sum_of_i_mu_i_upper_bound = Vec::new();
    let mut auxiliary_terms = Vec::new();

    for i in 0..lower_bound.len() {
        sum_of_i_mu_i_lower_bound.push(sum_of_i_mu_i(lower_bound[i] - 1, &sum_of_i_mu_i_small, &mut sum_of_i_mu_i_big));
        sum_of_i_mu_i_upper_bound.push(sum_of_i_mu_i(upper_bound[i], &sum_of_i_mu_i_small, &mut sum_of_i_mu_i_big));
    }

    for i in 0..n_over_ds.len() {
        auxiliary_terms.push((((n_over_ds[i] % MOD) * ((n_over_ds[i] + 1) % MOD)) % MOD * ((n_over_ds[i] + 1) % MOD)) % MOD);
    }

    let mut answer = 0;
    for i in 0..auxiliary_terms.len() {
        answer += auxiliary_terms[i] % MOD * (sum_of_i_mu_i_upper_bound[i] - sum_of_i_mu_i_lower_bound[i]) % MOD;
        answer = (answer + MOD) % MOD;
    }

    answer = (answer - 2 + MOD) % MOD;
    println!("{}", answer);
}
