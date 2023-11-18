# Green번 - 별 안에 별 안에 별 찍기

star_pattern = [
    (2, 0),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (1, 3),
    (2, 3),
    (3, 3),
    (1, 4),
    (3, 4),
]

N = int(input())
grid = [[" " for _ in range(5**N)] for _ in range(5**N)]
stack = [(0, 0, N)]
while stack:
    start_x, start_y, stage = stack.pop()
    if stage == 0:
        grid[start_y][start_x] = "*"
        continue
    for x_offset, y_offset in star_pattern:
        x_offset *= 5 ** (stage - 1)
        y_offset *= 5 ** (stage - 1)
        stack.append((start_x + x_offset, start_y + y_offset, stage - 1))
for v in grid:
    print(*v, sep="")