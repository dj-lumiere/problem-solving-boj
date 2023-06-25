# B번 - 초콜릿 보관함
from sys import stdin, stdout
from itertools import product

input = stdin.readline
print = stdout.write


def is_inbound(grid_size: tuple[int, int], current_pos: tuple[int, int]) -> bool:
    return all([0 <= pos < size for pos, size in zip(current_pos, grid_size)])


def dfs(
    grid: list[list[str]], grid_size: tuple[int, int], starting_pos: tuple[int, int]
) -> int:
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dfs_stack = [starting_pos]
    cluster_size = 0
    while dfs_stack:
        current_x_pos, current_y_pos = dfs_stack.pop()
        if grid[current_y_pos][current_x_pos] == "O":
            cluster_size += 1
            grid[current_y_pos][current_x_pos] = "X"
        for dx, dy in delta:
            next_x_pos, next_y_pos = current_x_pos + dx, current_y_pos + dy
            if not is_inbound(grid_size, (next_x_pos, next_y_pos)):
                continue
            if grid[next_y_pos][next_x_pos] == "X":
                continue
            if grid[next_y_pos][next_x_pos] == "-":
                continue
            dfs_stack.append((next_x_pos, next_y_pos))
    return cluster_size


def connected_chocolate_group(
    grid: list[list[str]], grid_size: tuple[int, int]
) -> list[int]:
    result = []
    x_size, y_size = grid_size
    for x, y in product(range(x_size), range(y_size)):
        if grid[y][x] == "O":
            result.append(dfs(grid, grid_size, (x, y)))
    result.sort()
    return result


T = int(input())
for _ in range(T):
    grid = [list(input().strip()) for _ in range(3)]
    n, *a = list(map(int, input().strip().split(" ")))
    if connected_chocolate_group(grid, (3, 3)) == a:
        print("1\n")
    else:
        print("0\n")