use std::collections::HashMap;
use std::io;
use std::io::{Read, Write};


pub(crate) fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: i32 = tokens.next().unwrap().parse().unwrap();
    let m: i32 = tokens.next().unwrap().parse().unwrap();
    let mut grid: Vec<Vec<i32>> = (0..n).map(|_| (0..n).map(|_| tokens.next().unwrap().parse().unwrap()).collect::<Vec<i32>>()).collect::<Vec<Vec<i32>>>();
    let magic: Vec<(i32, i32)> = (0..m).map(|_| (tokens.next().unwrap().parse().unwrap(), tokens.next().unwrap().parse().unwrap())).collect::<Vec<(i32, i32)>>();
    //println!("{:?}", grid);
    let mut grid_order: Vec<Vec<i32>> = (0..n).map(|_| vec![0; n as usize]).collect::<Vec<Vec<i32>>>();
    let movement_order: Vec<(i32, i32)> = vec![(1, 0), (0, 1), (-1, 0), (0, -1)];
    let magic_order: Vec<(i32, i32)> = vec![(0, -1), (0, 1), (-1, 0), (1, 0)];
    let mut stack: Vec<(i32, i32, i32)> = vec![(0, 0, 0)];
    grid_order[0][0] = 1;
    while !stack.is_empty() {
        let (x, y, dir) = stack.pop().unwrap();
        if x == n / 2 && y == n / 2 {
            break;
        }
        if !(0 <= x + movement_order[dir as usize].0 && x + movement_order[dir as usize].0 < n && 0 <= y + movement_order[dir as usize].1 && y + movement_order[dir as usize].1 < n) {
            stack.push((x, y, (dir + 1) % 4));
            continue;
        }
        if grid_order[(y + movement_order[dir as usize].1) as usize][(x + movement_order[dir as usize].0) as usize] != 0 {
            stack.push((x, y, (dir + 1) % 4));
            continue;
        }
        grid_order[(y + movement_order[dir as usize].1) as usize][(x + movement_order[dir as usize].0) as usize] = grid_order[y as usize][x as usize] + 1;
        stack.push((x + movement_order[dir as usize].0, y + movement_order[dir as usize].1, dir));
    }
    let mut grid_map: HashMap<(usize, usize), i32> = HashMap::new();
    for i in 0..n as usize {
        for j in 0..n as usize {
            grid_map.insert((i, j), grid_order[j][i]);
        }
    }
    let mut grid_to_line: Vec<i32> = vec![0; (n * n) as usize];
    for i in 0..n as usize {
        for j in 0..n as usize {
            grid_to_line[(grid_order[j][i] - 1) as usize] = grid[j][i];
        }
    }
    grid_to_line.pop();
    // println!("라인 펼침\n{:?}", grid_to_line);
    let mut exploded_beads = vec![0; 4];
    for &(d, s) in &magic {
        let magic_dir = magic_order[(d - 1) as usize];
        for i in 1..=s {
            grid_to_line[(grid_order[(n / 2 + magic_dir.1 * i) as usize][(n / 2 + magic_dir.0 * i) as usize] - 1) as usize] = 0;
        }
        // println!("마법 사용\n{:?}", grid_to_line);
        grid_to_line = grid_to_line.iter().enumerate().filter(|(_i, &v)| v != 0).map(|(_i, &v)| v).collect::<Vec<i32>>();
        // println!("구슬 모음\n{:?}", grid_to_line);
        let mut iteration_count = 1;
        while true {
            grid_to_line.push(-1);
            let mut last_chain_position = 0;
            let mut last_item = 0;
            let mut has_chain = false;
            for i in 0..grid_to_line.len() {
                if i == 0 {
                    last_item = grid_to_line[i];
                    continue;
                }
                let mut v = grid_to_line[i];
                if v != last_item {
                    // println!("{} {}", last_chain_position, i);
                    if i - last_chain_position >= 4 {
                        has_chain = true;
                        exploded_beads[grid_to_line[i - 1] as usize] += i - last_chain_position;
                        for j in last_chain_position..i {
                            grid_to_line[j] = 0;
                        }
                    }
                    last_item = v;
                    last_chain_position = i;
                    continue;
                }
            }
            // println!("구슬 폭발 {}회차\n{:?}", iteration_count, grid_to_line);
            grid_to_line = grid_to_line.iter().enumerate().filter(|(_i, &v)| v != 0).map(|(_i, &v)| v).collect::<Vec<i32>>();
            grid_to_line.pop();
            // println!("{:?}", grid_to_line);
            iteration_count += 1;
            if !has_chain { break; }
        }
        grid_to_line.insert(0, -1);
        let mut grid_after_change = vec![0; (n * n - 1) as usize];
        let mut last_chain_position = 0;
        let mut last_item = 0;
        let mut current_position = 0;
        for (i, &v) in grid_to_line.iter().rev().enumerate() {
            if i == 0 {
                last_item = v;
                continue;
            }
            if v != last_item {
                // println!("{} {} {} {}", i, v, last_chain_position, last_item);
                if current_position >= n * n - 2 {
                    break;
                }
                grid_after_change[(n * n - 2 - current_position) as usize] = (i - last_chain_position) as i32;
                grid_after_change[(n * n - 2 - (current_position + 1)) as usize] = last_item;
                last_chain_position = i;
                last_item = v;
                current_position += 2;
                continue;
            }
        }
        grid_to_line = grid_after_change;
        // println!("블리자드 완료 후\n{:?}", grid_to_line);
    }
    //println!("{:?}", exploded_beads);
    let answer = exploded_beads.iter().enumerate().map(|(i, &v)| i * v).fold(0, |x, y| x + y);
    println!("{}", answer);
}