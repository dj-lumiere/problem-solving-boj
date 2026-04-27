use std::io;
use std::io::{Read, Write};

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n = tokens.next().unwrap().parse::<i32>().unwrap();
    let s:String = tokens.next().unwrap().parse::<String>().unwrap();
    let mut answer = 0;
    for _ in 0..n{
        let mut name:Vec<&str> = tokens.next().unwrap().split("_").collect();
        let count:i32 = tokens.next().unwrap().parse::<i32>().unwrap();
        let mut matched:bool = false;
        for word in name.iter(){
            if **word == s && !matched{
                answer += count;
                matched = true;
            }
        }
    }
    println!("{}", answer);
}