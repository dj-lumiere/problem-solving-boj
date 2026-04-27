use std::cmp::min;
use std::io;
use std::io::{Read, Write};

pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let a: i64 = tokens.next().unwrap().parse().unwrap();
    let b: i64 = tokens.next().unwrap().parse().unwrap();
    let c: i64 = tokens.next().unwrap().parse().unwrap();
    let d: i64 = tokens.next().unwrap().parse().unwrap();
    let k: i64 = tokens.next().unwrap().parse().unwrap();
    let speed_stop = if k == 0 { 2 * 10i64.pow(12) } else { b / k };
    let toca_distance = |t: i64| -> i64{
        let move_iteration = min(speed_stop, t - 1);
        (2i64 * b - k * move_iteration) * (move_iteration + 1) / 2
    };
    let doldol_distance = |t: i64| -> i64{ d * t };
    let toca_position = |t: i64| -> i64 { min(0, toca_distance(t) - a) };
    let doldol_position = |t: i64| -> i64 { min(0, doldol_distance(t) - a - c) };
    let mut start: i64 = 0;
    let mut end: i64 = 2 * 10i64.pow(12) + 1;
    while start + 1 < end {
        let mid: i64 = (start + end) / 2;
        if toca_distance(mid) >= a {
            end = mid;
        } else {
            start = mid;
        }
    }
    let mut toca_arrive = end;
    start = 0;
    end = toca_arrive + 1;
    while start + 1 < end {
        let mid: i64 = (start + end) / 2;
        if toca_position(mid) <= doldol_position(mid) {
            end = mid;
        } else {
            start = mid;
        }
    }
    println!("{}", if end == toca_arrive + 1 { toca_arrive } else { -1 });
}