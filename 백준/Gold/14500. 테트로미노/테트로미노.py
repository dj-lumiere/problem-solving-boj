# 14500 테트로미노

from itertools import product

grid_2by3 = [
    [[0, 1], [1, 1], [0, 1]],
    [[1, 0], [1, 1], [1, 0]],
    [[1, 1], [1, 0], [1, 0]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 1], [0, 1], [0, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 0], [1, 1], [0, 1]],
]
grid_3by2 = [
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
]


grid_height, grid_width = map(int, input().split(" "))
grid = [list(map(int, input().split(" "))) for _ in range(grid_height)]
maximum_sum = 0

for x, y in product(range(grid_width), range(grid_height)):
    # 1*4 체크
    if y + 4 > grid_height:
        continue
    sub_sum = sum([grid[y + dy][x] for dy in range(4)])
    maximum_sum = max(sub_sum, maximum_sum)
for x, y in product(range(grid_width), range(grid_height)):
    # 4*1 체크
    if x + 4 > grid_width:
        continue
    sub_sum = sum([grid[y][x + dx] for dx in range(4)])
    maximum_sum = max(sub_sum, maximum_sum)
for x, y in product(range(grid_width), range(grid_height)):
    # 2*2 체크
    if x + 2 > grid_width or y + 2 > grid_height:
        continue
    sub_sum = sum([grid[y + dy][x + dx] for dy, dx in product(range(2), range(2))])
    maximum_sum = max(sub_sum, maximum_sum)
for x, y in product(range(grid_width), range(grid_height)):
    # 2*3 체크
    if x + 2 > grid_width or y + 3 > grid_height:
        continue
    for tetromino in grid_2by3:
        sub_sum = sum(
            [
                grid[y + dy][x + dx] * tetromino[dy][dx]
                for dy, dx in product(range(3), range(2))
            ]
        )
        maximum_sum = max(sub_sum, maximum_sum)
for x, y in product(range(grid_width), range(grid_height)):
    # 3*2 체크
    if x + 3 > grid_width or y + 2 > grid_height:
        continue
    for tetromino in grid_3by2:
        sub_sum = sum(
            [
                grid[y + dy][x + dx] * tetromino[dy][dx]
                for dy, dx in product(range(2), range(3))
            ]
        )
        maximum_sum = max(sub_sum, maximum_sum)
print(f"{maximum_sum}")
