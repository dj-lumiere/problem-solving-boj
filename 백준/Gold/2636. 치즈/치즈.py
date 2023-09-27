# 2636 치즈

from itertools import product


def is_inbound(x_pos: int, x_size: int, y_pos: int, y_size: int) -> bool:
    return 0 <= x_pos < x_size and 0 <= y_pos < y_size


def find_outer_air_pocket(
    grid: list[list[int]], x_size: int, y_size: int
) -> list[list[int]]:
    DELTA: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack: list[tuple[int, int]] = [(0, 0)]
    outer_air_grid = [[0] * x_size for _ in range(y_size)]
    visited = [[False] * x_size for _ in range(y_size)]
    while stack:
        x_pos, y_pos = stack.pop()
        outer_air_grid[y_pos][x_pos] = 1
        visited[y_pos][x_pos] = True
        for dx, dy in DELTA:
            next_x_pos, next_y_pos = x_pos + dx, y_pos + dy
            if not is_inbound(next_x_pos, x_size, next_y_pos, y_size):
                continue
            if visited[next_y_pos][next_x_pos]:
                continue
            if grid[next_y_pos][next_x_pos] == 1:
                continue
            stack.append((next_x_pos, next_y_pos))
    return outer_air_grid


def remove_cheese_iteration(
    cheese: list[tuple[int, int]],
    outer_air_pocket: list[list[int]],
    grid: list[list[int]],
    x_size: int,
    y_size: int,
) -> tuple[list[tuple[int, int]], int]:
    DELTA: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = cheese
    not_removed = []
    removed = []
    while stack:
        x_pos, y_pos = stack.pop()
        contacted_side = 0
        for dx, dy in DELTA:
            next_x_pos, next_y_pos = x_pos + dx, y_pos + dy
            if not is_inbound(next_x_pos, x_size, next_y_pos, y_size):
                continue
            if (
                grid[next_y_pos][next_x_pos] == 0
                and outer_air_pocket[next_y_pos][next_x_pos] == 1
            ):
                contacted_side += 1
        if contacted_side >= 1:
            removed.append((x_pos, y_pos))
            continue
        not_removed.append((x_pos, y_pos))
    for x_pos, y_pos in removed:
        grid[y_pos][x_pos] = 0
    return not_removed, len(not_removed)


y_size, x_size = map(int, input().split(" "))
grid: list[list[int]] = [list(map(int, input().split(" "))) for _ in range(y_size)]
cheese: list[tuple[int, int]] = []
for x, y in product(range(x_size), range(y_size)):
    if grid[y][x] == 1:
        cheese.append((x, y))
cheese_count = len(cheese)
time = 0
last_cheese_count = cheese_count
while cheese_count != 0:
    outer_air = find_outer_air_pocket(grid, x_size, y_size)
    cheese, cheese_count = remove_cheese_iteration(
        cheese, outer_air, grid, x_size, y_size
    )
    if cheese_count != 0:
        last_cheese_count = cheese_count
    time += 1
print(time)
print(last_cheese_count)