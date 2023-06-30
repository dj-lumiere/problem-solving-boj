# 10991 별 찍기 - 16
from itertools import product

N = int(input())
# 그리드 하나 만들기
grid = [[" " for _ in range(2 * N - 1)] for _ in range(N)]
for x, y in product(range(2 * N - 1), range(N)):
    if (x + y) % 2 != N % 2:
        grid[y][x] = "*"
for i in range(N - 1):
    for j in range(N - 1 - i):
        grid[i][j] = " "
    for j in range(N + i, 2 * N - 1):
        grid[i][j] = ""
print(*["".join(i) for i in grid], sep="\n")