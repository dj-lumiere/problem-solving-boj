use std::collections::VecDeque;

fn is_inbound(x_pos: i32, x_size: i32, y_pos: i32, y_size: i32) -> bool {
    0 <= x_pos && x_pos < x_size && 0 <= y_pos && y_pos < y_size
}

fn bfs(visited: &mut Vec<Vec<Vec<i32>>>, x_size: i32, y_size: i32, wall_break_max: i32, graph: &Vec<Vec<i32>>) -> i32 {
    let mut bfs_deque: VecDeque<(i32, i32, i32)> = VecDeque::new();
    bfs_deque.push_back((0, 0, 0));
    visited[0][0][0] = 1;
    let delta = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];
    while let Some((x, y, broken_walls)) = bfs_deque.pop_front() {
        if x + 1 == x_size && y + 1 == y_size {
            return visited[y as usize][x as usize][broken_walls as usize];
        }
        for (dx, dy) in &delta {
            let nx = x + dx;
            let ny = y + dy;
            if !is_inbound(nx, x_size, ny, y_size) {
                continue;
            }
            if graph[ny as usize][nx as usize] == 0 && visited[ny as usize][nx as usize][broken_walls as usize] == 0 {
                visited[ny as usize][nx as usize][broken_walls as usize] = visited[y as usize][x as usize][broken_walls as usize] + 1;
                bfs_deque.push_back((nx, ny, broken_walls));
            } else if broken_walls < wall_break_max && graph[ny as usize][nx as usize] == 1 {
                visited[ny as usize][nx as usize][broken_walls as usize + 1] = visited[y as usize][x as usize][broken_walls as usize] + 1;
                bfs_deque.push_back((nx, ny, broken_walls + 1));
            }
        }
    }
    -1
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
    let n = iter.next().unwrap();
    let m = iter.next().unwrap();
    let k = 1;
    let mut graph: Vec<Vec<i32>> = Vec::new();
    for _ in 0..n {
        let mut row = String::new();
        std::io::stdin().read_line(&mut row).unwrap();
        let row: Vec<i32> = row.trim().chars().map(|x| x.to_digit(10).unwrap() as i32).collect();
        graph.push(row);
    }
    let mut visited: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; (k + 1) as usize]; m as usize]; n as usize];
    println!("{}", bfs(&mut visited, m, n, k, &graph));
}
