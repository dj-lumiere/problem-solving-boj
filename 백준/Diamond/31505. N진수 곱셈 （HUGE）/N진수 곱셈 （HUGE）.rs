use std::io;
use std::io::{Read, Write};

const MOD: i64 = 1002772198720536577;

const MOD1: i32 = 998244353;
const MOD1_MULINV: i32 = 669690699;
const ROOT1: i32 = 3;

const MOD2: i32 = 1004535809;
const MOD2_MULINV: i32 = 332747959;
const ROOT2: i32 = 3;

fn merge_remainder(remainder1: i32, remainder2: i32) -> i64 {
    let t1 = multiply_mod1(remainder1, MOD2_MULINV) as i64;
    let t2 = multiply_mod2(remainder2, MOD1_MULINV) as i64;
    let mut t1 = t1 * MOD2 as i64;
    let mut t2 = t2 * MOD1 as i64;
    t1 %= MOD;
    t2 %= MOD;
    t1 += t2;
    t1 %= MOD;
    if t1 >= 8e17 as i64 {
        t1 -= MOD;
    }
    t1
}

fn find_bit_ceil(a: i32) -> i32 {
    (a as f64).log2().ceil() as i32
}

fn bit_reversal_permutation(a: &mut Vec<i32>) {
    let n = a.len() as i32;
    for i in 1..n {
        let j = ((i as u32).reverse_bits() >> (32 - (n as f64).log2() as i32)) as i32;
        if i < j {
            a.swap(i as usize, j as usize);
        }
    }
}

fn polynomial_multiplication(a: &mut Vec<i32>, b: &mut Vec<i32>) -> Vec<i64> {
    let original_size = a.len() + b.len();
    let n = 1 << find_bit_ceil(original_size as i32);
    let mut result = vec![0; original_size];

    let mut transform_a_mod1 = a.clone();
    transform_a_mod1.resize(n, 0);

    let mut transform_b_mod1 = b.clone();
    transform_b_mod1.resize(n, 0);

    let mut transform_a_mod2 = a.clone();
    transform_a_mod2.resize(n, 0);

    let mut transform_b_mod2 = b.clone();
    transform_b_mod2.resize(n, 0);

    for i in 0..n {
        if transform_a_mod1[i] < 0 {
            transform_a_mod1[i] += MOD1;
        }
        if transform_a_mod2[i] < 0 {
            transform_a_mod2[i] += MOD2;
        }
        if transform_b_mod1[i] < 0 {
            transform_b_mod1[i] += MOD1;
        }
        if transform_b_mod2[i] < 0 {
            transform_b_mod2[i] += MOD2;
        }
    }

    transform_mod1(&mut transform_a_mod1, false);
    transform_mod1(&mut transform_b_mod1, false);
    transform_mod2(&mut transform_a_mod2, false);
    transform_mod2(&mut transform_b_mod2, false);

    for i in 0..n {
        transform_a_mod1[i] = multiply_mod1(transform_a_mod1[i], transform_b_mod1[i]);
        transform_a_mod2[i] = multiply_mod2(transform_a_mod2[i], transform_b_mod2[i]);
    }

    transform_mod1(&mut transform_a_mod1, true);
    transform_a_mod1.resize(original_size, 0);

    transform_mod2(&mut transform_a_mod2, true);
    transform_a_mod2.resize(original_size, 0);

    for i in 0..original_size {
        result[i] = merge_remainder(transform_a_mod1[i], transform_a_mod2[i]);
    }

    result
}

fn multiply_mod1(a: i32, b: i32) -> i32 {
    (a as u64 * b as u64 % MOD1 as u64) as i32
}

fn power_with_mod1(base: i32, index: i32) -> i32 {
    let mut answer = 1;
    let mut base = base;
    let mut index = index;
    while index > 0 {
        if index & 1 != 0 {
            answer = multiply_mod1(answer, base);
        }
        base = multiply_mod1(base, base);
        index >>= 1;
    }
    answer
}

fn modular_inverse1(base: i32) -> i32 {
    power_with_mod1(base, MOD1 - 2)
}

fn coefficient_normalization1(a: &mut Vec<i32>) {
    let n = a.len() as i32;
    let n_inv = modular_inverse1(n);
    for i in 0..n {
        a[i as usize] = multiply_mod1(a[i as usize], n_inv);
    }
}

fn transform_mod1(a: &mut Vec<i32>, invert: bool) {
    let n = a.len() as i32;
    bit_reversal_permutation(a);
    let mut root_of_unity = vec![0; (n / 2) as usize];
    let mut angle = (MOD1 - 1) / n;
    if invert {
        angle = MOD1 - 1 - angle;
    }
    root_of_unity[0] = 1;
    let angleth_power = power_with_mod1(ROOT1, angle);
    for i in 1..(n / 2) {
        root_of_unity[i as usize] = multiply_mod1(root_of_unity[(i - 1) as usize], angleth_power);
    }
    let mut len = 2;
    while len <= n {
        let step = n / len;
        for i in (0..n).step_by(len as usize) {
            for j in 0..(len / 2) {
                let u = a[(i + j) as usize];
                let v = multiply_mod1(a[(i + j + len / 2) as usize], root_of_unity[(step * j) as usize]);
                a[(i + j) as usize] = u + v;
                a[(i + j + len / 2) as usize] = u - v;
                if u + v >= MOD1 {
                    a[(i + j) as usize] -= MOD1;
                }
                if u - v < 0 {
                    a[(i + j + len / 2) as usize] += MOD1;
                }
            }
        }
        len <<= 1;
    }
    if invert {
        coefficient_normalization1(a);
    }
}

fn multiply_mod2(a: i32, b: i32) -> i32 {
    (a as u64 * b as u64 % MOD2 as u64) as i32
}

fn power_with_mod2(base: i32, index: i32) -> i32 {
    let mut answer = 1;
    let mut base = base;
    let mut index = index;
    while index > 0 {
        if index & 1 != 0 {
            answer = multiply_mod2(answer, base);
        }
        base = multiply_mod2(base, base);
        index >>= 1;
    }
    answer
}

fn modular_inverse2(base: i32) -> i32 {
    power_with_mod2(base, MOD2 - 2)
}

fn coefficient_normalization2(a: &mut Vec<i32>) {
    let n = a.len() as i32;
    let n_inv = modular_inverse2(n);
    for i in 0..n {
        a[i as usize] = multiply_mod2(a[i as usize], n_inv);
    }
}

fn transform_mod2(a: &mut Vec<i32>, invert: bool) {
    let n = a.len() as i32;
    bit_reversal_permutation(a);
    let mut root_of_unity = vec![0; (n / 2) as usize];
    let mut angle = (MOD2 - 1) / n;
    if invert {
        angle = MOD2 - 1 - angle;
    }
    root_of_unity[0] = 1;
    let angleth_power = power_with_mod2(ROOT2, angle);
    for i in 1..(n / 2) {
        root_of_unity[i as usize] = multiply_mod2(root_of_unity[(i - 1) as usize], angleth_power);
    }
    let mut len = 2;
    while len <= n {
        let step = n / len;
        for i in (0..n).step_by(len as usize) {
            for j in 0..(len / 2) {
                let u = a[(i + j) as usize];
                let v = multiply_mod2(a[(i + j + len / 2) as usize], root_of_unity[(step * j) as usize]);
                a[(i + j) as usize] = u + v;
                a[(i + j + len / 2) as usize] = u - v;
                if u + v >= MOD2 {
                    a[(i + j) as usize] -= MOD2;
                }
                if u - v < 0 {
                    a[(i + j + len / 2) as usize] += MOD2;
                }
            }
        }
        len <<= 1;
    }
    if invert {
        coefficient_normalization2(a);
    }
}

fn convert_to_n_ary(answer: &mut Vec<i64>, n: i32) {
    if n < 0 {
        answer.push(0);
    }
    for i in 0..answer.len() {
        if i + 1 == answer.len() {
            break;
        }
        answer[i + 1] += answer[i] / (n * n * n) as i64;
        answer[i] %= (n * n * n) as i64;
        if answer[i] >= -(n * n * n + n * n + n) as i64 && n < 0 {
            answer[i] += (n * n * n) as i64;
            answer[i + 1] -= 1;
        } else if answer[i] < -(n * n + n) as i64 && n < 0 {
            answer[i] -= (n * n * n) as i64;
            answer[i + 1] += 1;
        }
    }
    while !answer.is_empty() && answer.last() == Some(&0) {
        answer.pop();
    }
    if answer.is_empty() {
        answer.push(0);
    }
}

fn big_n_ary_multiplication(a: &mut Vec<i32>, b: &mut Vec<i32>, n: i32, is_minus_sign: bool) {
    let mut result = polynomial_multiplication(a, b);
    convert_to_n_ary(&mut result, n);
    let mut answer: Vec<char> = vec![0 as char; result.len() * 3 + 6];
    let mut ptr: i32 = 0;
    if is_minus_sign && (result.len() != 1 || result[0] != 0) {
        answer[0] = '~';
        ptr += 1;
    }

    for (i, &rit) in result.iter().rev().enumerate() {
        let mut first_digit: i64 = 0;
        let mut second_digit: i64 = 0;
        let mut third_digit: i64 = rit;
        second_digit = third_digit / n as i64;
        third_digit %= n as i64;
        if third_digit < 0 && n < 0 {
            second_digit += 1;
            third_digit -= n as i64;
        }
        first_digit = second_digit / n as i64;
        second_digit %= n as i64;
        if second_digit < 0 && n < 0 {
            first_digit += 1;
            second_digit -= n as i64;
        }
        if i == 0 {
            if first_digit == 0 && second_digit == 0 {
                answer[ptr as usize] = (third_digit + '!' as i64) as u8 as char;
                ptr += 1;
            } else if first_digit == 0 {
                answer[ptr as usize] = (second_digit + '!' as i64) as u8 as char;
                ptr += 1;
                answer[ptr as usize] = (third_digit + '!' as i64) as u8 as char;
                ptr += 1;
            } else {
                answer[ptr as usize] = (first_digit + '!' as i64) as u8 as char;
                ptr += 1;
                answer[ptr as usize] = (second_digit + '!' as i64) as u8 as char;
                ptr += 1;
                answer[ptr as usize] = (third_digit + '!' as i64) as u8 as char;
                ptr += 1;
            }
            continue;
        }
        answer[ptr as usize] = (first_digit + '!' as i64) as u8 as char;
        ptr += 1;
        answer[ptr as usize] = (second_digit + '!' as i64) as u8 as char;
        ptr += 1;
        answer[ptr as usize] = (third_digit + '!' as i64) as u8 as char;
        ptr += 1;
    }
    while !answer.is_empty() && answer.last() == Some(&(0 as char)) {
        answer.pop();
    }
    io::stdout().write_all(answer.iter().map(|s| s.to_string()).collect::<Vec<String>>().join("").as_bytes()).unwrap();
}

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: i32 = tokens.next().unwrap().parse().unwrap();
    let a: String = tokens.next().unwrap().parse().unwrap();
    let b: String = tokens.next().unwrap().parse().unwrap();
    let mut is_minus_sign = false;
    let mut a_list: Vec<i32> = Vec::new();
    let mut b_list: Vec<i32> = Vec::new();
    let mut i = -1;
    for (j, c) in a.chars().rev().enumerate() {
        if j + 1 == a.len() && c == '~' {
            is_minus_sign ^= true;
            break;
        }
        if j % 3 == 0 {
            a_list.push(c as i32 - '!' as i32);
            i += 1;
        } else if j % 3 == 1 {
            a_list[i as usize] += (c as i32 - '!' as i32) * n;
        } else if j % 3 == 2 {
            a_list[i as usize] += (c as i32 - '!' as i32) * n * n;
        }
    }
    i = -1;
    for (j, c) in b.chars().rev().enumerate() {
        if j + 1 == b.len() && c == '~' {
            is_minus_sign ^= true;
            break;
        }
        if j % 3 == 0 {
            b_list.push(c as i32 - '!' as i32);
            i += 1;
        } else if j % 3 == 1 {
            b_list[i as usize] += (c as i32 - '!' as i32) * n;
        } else if j % 3 == 2 {
            b_list[i as usize] += (c as i32 - '!' as i32) * n * n;
        }
    }
    big_n_ary_multiplication(&mut a_list, &mut b_list, n, is_minus_sign);
}