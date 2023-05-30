use std::collections::HashSet;
use std::io;

fn extended_gcd(a: i64, b: i64) -> (i64, i64, i64) {
    if a == 0 {
        (b, 0, 1)
    } else {
        let (g, x, y) = extended_gcd(b % a, a);
        (g, y - (b / a) * x, x)
    }
}

fn modular_inverse(a: i64, m: i64) -> i64 {
    let (g, x, _) = extended_gcd(a, m);
    if g != 1 {
        0 // modular inverse does not exist
    } else {
        (x % m + m) % m // making sure it's positive
    }
}

fn gcd(mut target1: i64, mut target2: i64) -> i64 {
    if target1 < target2 {
        std::mem::swap(&mut target1, &mut target2);
    }
    while target2 != 0 {
        target1 = target1 % target2;
        if target1 < target2 {
            std::mem::swap(&mut target1, &mut target2);
        }
    }
    return target1;
}

fn lcm(target1: i64, target2: i64) -> i64 {
    return target1 * target2 / gcd(target1, target2);
}

fn crt(mod_list: &Vec<i64>, residue_list: Vec<i64>) -> i64 {
    if (mod_list.len() == 1) && (residue_list.len() == 1) {
        return residue_list[0] % mod_list[0];
    }
    let all_lcm: i64 = mod_list.iter().fold(1, |acc: i64, &x| lcm(acc, x));
    let mut result: i64 = 0;
    for (i, j) in mod_list.iter().zip(residue_list) {
        result += j * ((all_lcm / i) as i64) * modular_inverse((all_lcm / *i) as i64, *i);
    }
    return result % all_lcm;
}

fn parse_mod_tester(digit_list: &Vec<i64>) -> Vec<i64> {
    let digits: HashSet<i64> = digit_list
        .into_iter()
        .filter(|&&i| i != 0)
        .map(|&x| x)
        .collect();
    let mut mod_test: Vec<i64> = vec![];
    if digits.contains(&8) {
        mod_test.push(8);
    } else if digits.contains(&4) {
        mod_test.push(4);
    } else if digits.contains(&2) || digits.contains(&6) {
        mod_test.push(2);
    }
    if digits.contains(&9) {
        mod_test.push(9);
    } else if digits.contains(&3) || digits.contains(&6) {
        mod_test.push(3);
    }
    if digits.contains(&5) {
        mod_test.push(5);
    }
    if digits.contains(&7) {
        mod_test.push(7);
    }
    return mod_test;
}

fn solution(mod_test: &Vec<i64>, target_number: i64) -> i64 {
    if mod_test.len() == 0 {
        return target_number;
    }
    let mut test_value: i64 = target_number;
    let mut digit: u32 = 0;
    let mut residue: Vec<i64> = mod_test
        .iter()
        .map(|&modulus| (modulus - (test_value % modulus)) % modulus)
        .collect::<Vec<i64>>();
    if residue.iter().all(|&x| x == 0) {
        return test_value;
    }
    loop {
        test_value *= 10;
        digit += 1;
        residue = mod_test
            .iter()
            .map(|&modulus| (modulus - (test_value % modulus)) % modulus)
            .collect::<Vec<i64>>();
        let offset = crt(&mod_test, residue);
        if offset < (10_i64).pow(digit) {
            return test_value + offset;
        }
    }
}

fn main() {
    let mut s = String::new();
    let input = io::stdin();
    input.read_line(&mut s).unwrap();
    let n: i64 = s.trim().parse().unwrap();
    let digits: Vec<i64> = s
        .chars()
        .filter_map(|ch: char| ch.to_digit(10).map(|d: u32| d as i64))
        .collect();
    let mod_test: Vec<i64> = parse_mod_tester(&digits);
    let result: i64 = solution(&mod_test, n);
    println!("{}", result);
}
