# 14940 쉬운 최단거리
from collections import deque
from itertools import product

# BFS를 활용해 최단거리를 구하는 문제

grid_height, grid_width = map(int, input().split(" "))
grid = [list(map(int, input().split(" "))) for _ in range(grid_height)]
answer_grid = [[0] * grid_width for _ in range(grid_height)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
starting_point = [0, 0]

for y, x in product(range(grid_height), range(grid_width)):
    if grid[y][x] == 2:
        starting_point = [x, y]
        break

bfs_deque = deque([(starting_point[0], starting_point[1])])


def is_inbounds(pos_x: int, pos_y: int, grid_width: int, grid_height: int):
    return 0 <= pos_x < grid_width and 0 <= pos_y < grid_height


while bfs_deque:
    current_x, current_y = bfs_deque.popleft()
    for dx, dy in delta:
        next_x, next_y = current_x + dx, current_y + dy
        if not is_inbounds(
            pos_x=next_x, pos_y=next_y, grid_width=grid_width, grid_height=grid_height
        ):
            continue
        if grid[next_y][next_x] == 0:
            continue
        if grid[next_y][next_x] == 1:
            grid[next_y][next_x] = 0
            answer_grid[next_y][next_x] = answer_grid[current_y][current_x] + 1
        bfs_deque.append((next_x, next_y))

for y, x in product(range(grid_height), range(grid_width)):
    if grid[y][x] == 1 and answer_grid[y][x] == 0:
        answer_grid[y][x] = -1
print("\n".join([" ".join(map(str, i)) for i in answer_grid]))