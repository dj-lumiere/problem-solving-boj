use std::io;
use std::io::{Read, Write};

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let r = tokens.next().unwrap().parse().unwrap();
    let c = tokens.next().unwrap().parse().unwrap();
    println!("{}", (0..r).map(|_| "*".repeat(c)).collect::<Vec<_>>().join("\n"))
}