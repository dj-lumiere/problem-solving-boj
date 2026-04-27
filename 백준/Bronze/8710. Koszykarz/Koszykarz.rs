use std::io;
use std::io::Read;

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut k: i64 = tokens.next().unwrap().parse().unwrap();
    let mut w: i64 = tokens.next().unwrap().parse().unwrap();
    let mut m: i64 = tokens.next().unwrap().parse().unwrap();
    println!("{}", (w - k + m - 1) / m);
}
