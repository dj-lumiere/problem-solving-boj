# 10996 별 찍기 - 21
from itertools import product

N = int(input())
grid = [["*" for _ in range(N)] for _ in range(2 * N)]
for x, y in product(range(N), range(2 * N)):
    if (x + y) % 2:
        grid[y][x] = " "
for y in range(2 * N):
    if grid[y][-1] == " ":
        grid[y][-1] == ""
print(*["".join(i) for i in grid], sep="\n")