use std::io;
use std::io::{Read, stdout, Write};

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n = input.trim().parse::<i32>().unwrap();
    input.clear();
    let mut names: Vec<String> = Vec::new();
    let mut answer = String::new();
    for _ in 0..n {
        io::stdin().read_line(&mut input).unwrap();
        let name = input.trim().to_owned();
        names.push(name);
        input.clear();
    }
    input.clear();
    for name in names.iter() {
        println!("? {}", name);
        io::stdin().read_line(&mut input).unwrap();
        // println!("{:?}", input.to_owned().into_bytes().iter().collect::<Vec<&u8>>());
        let mut result1 = input.trim().parse::<i32>().unwrap();
        input.clear();
        println!("? {}", name);
        io::stdin().read_line(&mut input).unwrap();
        // println!("{:?}", input.to_owned().into_bytes().iter().collect::<Vec<&u8>>());
        let mut result2 = input.trim().parse::<i32>().unwrap();
        input.clear();
        if result1 == 1 || result2 == 1 {
            answer = name.to_string();
        }
    }
    // println!("{}", answer);
    println!("! {}", answer);
}