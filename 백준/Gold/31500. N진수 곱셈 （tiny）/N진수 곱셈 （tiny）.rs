use std::io;
use std::io::{Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: i64 = tokens.next().unwrap().parse().unwrap();
    let a_str: String = tokens.next().unwrap().parse().unwrap();
    let b_str: String = tokens.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = a_str.chars().rev().map(|s| s as i64 - '!' as i64).collect();
    let mut b: Vec<i64> = b_str.chars().rev().map(|s| s as i64 - '!' as i64).collect();
    let mut minus_sign = false;
    if *a.last().unwrap() == '~' as i64 - '!' as i64 {
        minus_sign ^= true;
        a.pop();
    }
    if *b.last().unwrap() == '~' as i64 - '!' as i64 {
        minus_sign ^= true;
        b.pop();
    }
    //println!("{:?}\n{:?}", a, b);
    let mut result: Vec<i64> = vec![0; a_str.len() + b_str.len() + 1];
    for (i1, &v1) in a.iter().enumerate() {
        for (i2, &v2) in b.iter().enumerate() {
            result[i1 + i2] += v1 * v2;
        }
    }
    for i in 0..result.len() - 1 {
        result[i + 1] += result[i] / n;
        result[i] %= n;
        if n < 0 && result[i] < 0 {
            result[i] -= n;
            result[i + 1] += 1;
        }
    }
    //println!("{:?}", result);
    while result.len() > 1 && *result.last().unwrap() == 0 {
        result.pop();
    }
    let result_str: String = result.iter().rev().map(|&s| (s as u8 + b'!') as char).collect();
    if minus_sign && (result.len() != 1 || result[0] != 0i64) {
        io::stdout().write("~".as_bytes()).unwrap();
    }
    io::stdout().write_all(result_str.as_bytes()).unwrap();
}