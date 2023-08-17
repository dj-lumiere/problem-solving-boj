# 16236 아기 상어

from collections import deque
from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def is_inbound(x_pos, x_size, y_pos, y_size) -> bool:
    return 0 <= x_pos < x_size and 0 <= y_pos < y_size


def bfs_iteration(N, current_x, current_y, distance, bfs_deque, edible, grid):
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in DELTA:
        nx, ny = current_x + dx, current_y + dy
        if not is_inbound(nx, N, ny, N):
            continue
        if distance[ny][nx] != -1:
            continue
        if 0 <= grid[ny][nx] <= shark_size:
            distance[ny][nx] = distance[current_y][current_x] + 1
            bfs_deque.append((nx, ny))
        if 0 < grid[ny][nx] < shark_size:
            edible.append((nx, ny))


def find_fish_to_eat(N, shark_x, shark_y, grid):
    distance = [[-1] * N for _ in range(N)]
    bfs_deque = deque([(shark_x, shark_y)])
    distance[shark_y][shark_x] = 0
    edible = []
    while bfs_deque:
        current_x, current_y = bfs_deque.popleft()
        bfs_iteration(N, current_x, current_y, distance, bfs_deque, edible, grid)
    if not edible:
        return None
    edible.sort(key=lambda x: (distance[x[1]][x[0]], x[1], x[0]))
    return edible[0], distance[edible[0][1]][edible[0][0]]


N = int(input())
grid = [list(map(int, input().split(" "))) for _ in range(N)]
shark_size = 2
fish_count = 0
remaining_fish_to_size_increase = shark_size
shark_x = 0
shark_y = 0
total_distance = 0
for x, y in product(range(N), repeat=2):
    if grid[y][x] == 9:
        shark_x, shark_y = x, y
        grid[y][x] = 0
while True:
    fish_to_eat = find_fish_to_eat(N, shark_x, shark_y, grid)
    if fish_to_eat == None:
        break
    (shark_x, shark_y), distance = fish_to_eat
    total_distance += distance
    fish_count += 1
    grid[shark_y][shark_x] = 0
    remaining_fish_to_size_increase -= 1
    if remaining_fish_to_size_increase == 0:
        shark_size += 1
        remaining_fish_to_size_increase = shark_size
print(f"{total_distance}")
