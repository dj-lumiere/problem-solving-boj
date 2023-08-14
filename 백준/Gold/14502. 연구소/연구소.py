# 14502 연구소
from itertools import combinations, product


def reset_grid(original_grid, grid, x_size, y_size):
    for i, j in product(range(y_size), range(x_size)):
        grid[i][j] = original_grid[i][j]


def is_inbound(pos_x, pos_y, x_size, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


def dfs(grid, virus_pos, x_size, y_size) -> int:
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = len(virus_pos)
    stack = virus_pos[:]
    while stack:
        pos_x, pos_y = stack.pop()
        if grid[pos_y][pos_x] != VIRUS:
            continue
        for dx, dy in DELTA:
            if not is_inbound(pos_x + dx, pos_y + dy, x_size, y_size):
                continue
            if grid[pos_y + dy][pos_x + dx] != BLANK:
                continue
            grid[pos_y + dy][pos_x + dx] = VIRUS
            stack.append((pos_x + dx, pos_y + dy))
            result += 1
    return result


BLANK = 0
WALL = 1
VIRUS = 2
y_size, x_size = map(int, input().split(" "))
blank_pos = []
virus_pos = []
wall_count = 0
max_safe_area = -1
original_grid = [list(map(int, input().split(" "))) for _ in range(y_size)]
grid = [[original_grid[i][j] for j in range(x_size)] for i in range(y_size)]
for i, j in product(range(y_size), range(x_size)):
    if original_grid[i][j] == BLANK:
        blank_pos.append((j, i))
    if original_grid[i][j] == VIRUS:
        virus_pos.append((j, i))
    if original_grid[i][j] == WALL:
        wall_count += 1
wall_count += 3
for (x1, y1), (x2, y2), (x3, y3) in combinations(blank_pos, 3):
    grid[y1][x1] = grid[y2][x2] = grid[y3][x3] = WALL
    safe_area_sub = x_size * y_size - dfs(grid, virus_pos, x_size, y_size) - wall_count
    max_safe_area = max(max_safe_area, safe_area_sub)
    reset_grid(original_grid, grid, x_size, y_size)
print(max_safe_area)