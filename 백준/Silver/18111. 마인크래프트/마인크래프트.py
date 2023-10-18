# 18111 마인크래프트
from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


N, M, B = map(int, input().split(" "))
ground_level = [list(map(int, input().split(" "))) for _ in range(N)]
cell_height_count = [0 for _ in range(257)]
for i, j in product(range(N), range(M)):
    cell_height_count[ground_level[i][j]] += 1
result = N * M * 256 * 2 + 1
result_sub = 0
blocks_to_fill = 0
timing = 0
for i, j in product(range(257), repeat=2):
    if j == 0:
        result_sub = 0
        blocks_to_fill = 0
    result_sub += ((i - j) if i > j else 2 * (j - i)) * cell_height_count[j]
    blocks_to_fill += (i - j) * cell_height_count[j]
    if j == 256:
        if blocks_to_fill > B:
            continue
        result = min(result, result_sub)
        if result == result_sub:
            timing = i
print(result, timing)