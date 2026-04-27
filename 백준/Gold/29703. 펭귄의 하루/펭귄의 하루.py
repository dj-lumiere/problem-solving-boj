# 29703 펭귄의 하루

from collections import deque
from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def is_inbound(x_pos, x_size, y_pos, y_size):
    return 0 <= x_pos < x_size and 0 <= y_pos < y_size


def find_fish(grid, N, M, cur_x, cur_y):
    queue = deque([(cur_x, cur_y)])
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance = [[-1 for _ in range(M)] for _ in range(N)]
    distance[cur_y][cur_x] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if not is_inbound(nx, M, ny, N):
                continue
            if distance[ny][nx] != -1:
                continue
            if grid[ny][nx] == "D":
                continue
            distance[ny][nx] = distance[y][x] + 1
            queue.append((nx, ny))
    for x, y in product(range(M), range(N)):
        if grid[y][x] != "F" or distance[y][x] == -1:
            distance[y][x] = 10**9
    return distance


N, M = map(int, input().split(" "))
grid = [list(input()) for _ in range(N)]

penguin_pos = [0, 0]
home_pos = [0, 0]
for i, j in product(range(M), range(N)):
    if grid[j][i] == "S":
        penguin_pos = [i, j]
    if grid[j][i] == "H":
        home_pos = [i, j]
start_to_fish_distance = find_fish(grid, N, M, *penguin_pos)
home_to_fish_distance = find_fish(grid, N, M, *home_pos)
minimal_distance = 2 * 10**9
for x, y in product(range(M), range(N)):
    minimal_distance = min(
        minimal_distance, start_to_fish_distance[y][x] + home_to_fish_distance[y][x]
    )
if minimal_distance >= 10**9:
    print(-1)
else:
    print(minimal_distance)