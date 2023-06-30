# 1100 하얀 칸
from itertools import product

grid = [list(input()) for _ in range(8)]
answer = 0
for x, y in product(range(8), range(8)):
    if not (x + y) % 2 and grid[y][x] == "F":
        answer += 1
print(answer)