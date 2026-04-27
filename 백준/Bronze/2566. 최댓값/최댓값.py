# 2566 최댓값

from itertools import product

grid = [list(map(int, input().split(" "))) for _ in range(9)]
result = [0, 0]
current_number = 0
for x, y in product(range(9), range(9)):
    if grid[y][x] > current_number:
        result = [x, y]
        current_number = grid[y][x]
print(f"{current_number}\n{result[1]+1} {result[0]+1}")