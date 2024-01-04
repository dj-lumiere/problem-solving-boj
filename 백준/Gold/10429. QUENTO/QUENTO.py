# 10429 QUENTO
from itertools import product

N, M = map(int, input().split())
grid = [list(input()) for _ in range(3)]
stack = [
    (1, 0, 0, [[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (1, 0, 2, [[0, 0, 1], [0, 0, 0], [0, 0, 0]]),
    (1, 1, 1, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    (1, 2, 0, [[0, 0, 0], [0, 0, 0], [1, 0, 0]]),
    (1, 2, 2, [[0, 0, 0], [0, 0, 0], [0, 0, 1]]),
]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_inbound(x_pos, y_pos):
    return 0 <= x_pos < 3 and 0 <= y_pos < 3


reached_result = False
while stack:
    visited_cells, y, x, visited = stack.pop()
    if reached_result:
        break
    if visited_cells == 2 * M - 1:
        cell_path = [(0, 0) for _ in range(2 * M - 1)]
        for x, y in product(range(3), repeat=2):
            if visited[y][x]:
                cell_path[visited[y][x] - 1] = (y, x)
        result = 0
        is_negative = False
        for y, x in cell_path:
            if grid[y][x] == "+":
                is_negative = False
            elif grid[y][x] == "-":
                is_negative = True
            else:
                result += int(grid[y][x]) * (-1 if is_negative else 1)
        if result == N:
            reached_result = True
            print(1)
            for x, y in cell_path:
                print(x, y)
            break
        else:
            continue
    for dx, dy in delta:
        if not is_inbound(x + dx, y + dy):
            continue
        if visited[y + dy][x + dx]:
            continue
        new_visited = [[visited[i][j] for j in range(3)] for i in range(3)]
        new_visited[y + dy][x + dx] = visited_cells + 1
        stack.append((visited_cells + 1, y + dy, x + dx, new_visited))
if not reached_result:
    print(0)
