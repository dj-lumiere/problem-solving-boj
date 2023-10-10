# 2447 별 찍기 - 10

from itertools import product

N = int(input())
grid = [["*" for _ in range(N)] for _ in range(N)]

for i, j in product(range(N), repeat=2):
    k = 1
    while k < N:
        if (i // k) % 3 == (j // k) % 3 == 1:
            grid[i][j] = " "
            break
        k *= 3

for v in grid:
    print(*v, sep="")