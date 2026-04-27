use std::io;
use std::io::{Read, Write};

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace().map(|s| s.parse().unwrap());
    let (n, q) = (tokens.next().unwrap(), tokens.next().unwrap());
    let mut a:Vec<i64> = vec![0; n];
    for i in 0..n{
        a[i] = tokens.next().unwrap() as i64;
    }
    let mut a_sum:Vec<i64> = Vec::new();
    let mut answer:Vec<String> = Vec::new();
    a_sum.push(0);
    for (_, &v) in a.iter().enumerate(){
        a_sum.push(*a_sum.last().unwrap() + v);
    }
    for (_, &v) in a.iter().enumerate(){
        a_sum.push(*a_sum.last().unwrap() + v);
    }
    let mut offset = 0;
    for _ in 0..q{
        let opcode = tokens.next().unwrap();
        match opcode{
            1=>{
                let k = tokens.next().unwrap();
                offset += n-k;
                offset %= n;
            }
            2=>{
                let k = tokens.next().unwrap();
                offset += k;
                offset %= n;
            }
            3=>{
                let (a, b) = (tokens.next().unwrap(), tokens.next().unwrap());
                answer.push((a_sum[b+offset]-a_sum[a+offset-1]).to_string());
            }
            _=>()
        }
    }
    io::stdout().write_all(answer.join("\n").as_bytes()).unwrap();
}