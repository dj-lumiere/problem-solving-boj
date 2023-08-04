# 24049 정원 (Easy)

from itertools import product

N, M = map(int, input().split(" "))
flower_grid = [[0] * (N + 1) for _ in range(M + 1)]
column_flower = list(map(int, input().split(" ")))
row_flower = list(map(int, input().split(" ")))
for i, v in enumerate(column_flower, start=1):
    flower_grid[0][i] = v
for i, v in enumerate(row_flower, start=1):
    flower_grid[i][0] = v
for r, c in product(range(1, M + 1), range(1, N + 1)):
    flower_grid[r][c] = flower_grid[r - 1][c] ^ flower_grid[r][c - 1]
print(flower_grid[-1][-1])