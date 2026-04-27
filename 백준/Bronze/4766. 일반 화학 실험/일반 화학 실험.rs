use std::io::{read_to_string, stdin};

fn main() {
    let input = &read_to_string(stdin()).unwrap();
    let mut scanner = input.split_whitespace().map(|s| s.parse::<f64>().map_err(|_| s.to_string()));
    let mut previous_value: f64 = 0f64;
    for (i, a) in scanner.enumerate() {
        let mut v = a.unwrap();
        if (v == 999f64) {
            break;
        }
        let difference = v - previous_value;
        if (i != 0) {
            println!("{0:.2}", difference);
        }
        previous_value = v;
    }
}