# 16724 피리 부는 사나이
# 집합의 갯수를 구하기

from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def is_inbound(pos_x, x_size, pos_y, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


N, M = map(int, input().split(" "))
map_info = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
DELTA = {"D": (0, 1), "U": (0, -1), "L": (-1, 0), "R": (1, 0)}

answer = 0
for y, x in product(range(N), range(M)):
    if visited[y][x] == 2:
        continue
    stack = [(x, y)]
    group = [(x, y)]
    while stack:
        x, y = stack.pop()
        if visited[y][x] == 0:
            visited[y][x] = 1
        dx, dy = DELTA[map_info[y][x]]
        nx, ny = x + dx, y + dy
        if not is_inbound(nx, M, ny, N):
            continue
        if visited[ny][nx] == 1:
            answer += 1
            for x, y in group:
                visited[y][x] = 2
            break
        if visited[ny][nx] == 2:
            for x, y in group:
                visited[y][x] = 2
            continue
        group.append((nx, ny))
        stack.append((nx, ny))
        visited[ny][nx] = 1

print(answer)