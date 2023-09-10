# 29733 3차원 지뢰찾기

from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def is_inbound(pos_x, x_size, pos_y, y_size, pos_z, z_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size and 0 <= pos_z < z_size


DELTA = list(
    [(i, j, k) for i, j, k in product(range(-1, 2), repeat=3) if any([i, j, k])]
)
R, C, H = map(int, input().split(" "))
grid = [[list(input()) for _ in range(R)] for _ in range(H)]
mine_count = [[["0" for _ in range(C)] for _ in range(R)] for _ in range(H)]
for c, r, h in product(range(C), range(R), range(H)):
    if grid[h][r][c] == "*":
        mine_count[h][r][c] = "*"
        continue
    mine_count_sub = 0
    for i, j, k in DELTA:
        nc, nr, nh = c + i, r + j, h + k
        if not is_inbound(nc, C, nr, R, nh, H):
            continue
        if grid[nh][nr][nc] == "*":
            mine_count_sub += 1
    mine_count[h][r][c] = str(mine_count_sub % 10)
for h, r in product(range(H), range(R)):
    print(*mine_count[h][r], sep="")
