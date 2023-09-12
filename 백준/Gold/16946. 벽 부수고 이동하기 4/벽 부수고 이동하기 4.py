# 16946 벽 부수고 이동하기 4

from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def is_inbound(x_pos, x_size, y_pos, y_size):
    return 0 <= x_pos < x_size and 0 <= y_pos < y_size


n, m = map(int, input().split(" "))
grid = [list(map(int, list(input()))) for _ in range(n)]
group = [[0 for _ in range(m)] for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]
group_info = dict()
group_count = 0
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for y, x in product(range(n), range(m)):
    if grid[y][x] != 0:
        continue
    if group[y][x] != 0:
        continue
    group_count += 1
    item_count = 0
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if group[y][x] == 0:
            group[y][x] = group_count
            item_count += 1
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if not is_inbound(nx, m, ny, n):
                continue
            if grid[ny][nx] == 1:
                continue
            if group[ny][nx] != 0:
                continue
            stack.append((nx, ny))
    group_info[group_count] = item_count

for y, x in product(range(n), range(m)):
    if not grid[y][x]:
        continue
    result = 1
    visited_set = set()
    for dx, dy in DELTA:
        nx, ny = x + dx, y + dy
        if not is_inbound(nx, m, ny, n):
            continue
        if not group[ny][nx]:
            continue
        if group[ny][nx] in visited_set:
            continue
        visited_set.add(group[ny][nx])
        result += group_info[group[ny][nx]]
    answer[y][x] = result % 10

for y in range(n):
    print(*answer[y], sep="")