# B번 - 여중생 파댕이와 공부를
from itertools import product


def score_operation(grid: list[list[str]], start_x: int, start_y: int):
    formula = grid[start_y + 1][start_x + 1 : start_x + 7]
    if formula[-1] == ".":
        formula.pop()
    a, b, c = int(formula[0]), int(formula[2]), int("".join(formula[4:]))
    is_correct = a + b == c
    if is_correct and len(formula) == 5:
        grid[start_y][start_x + 1 : start_x + 6] = ["*"] * 5
        grid[start_y + 2][start_x + 1 : start_x + 6] = ["*"] * 5
        grid[start_y + 1][start_x] = "*"
        grid[start_y + 1][start_x + 6] = "*"
    elif is_correct and len(formula) == 6:
        grid[start_y][start_x + 1 : start_x + 7] = ["*"] * 6
        grid[start_y + 2][start_x + 1 : start_x + 7] = ["*"] * 6
        grid[start_y + 1][start_x] = "*"
        grid[start_y + 1][start_x + 7] = "*"
    else:
        grid[start_y][start_x + 3] = "/"
        grid[start_y + 1][start_x + 2] = "/"
        grid[start_y + 2][start_x + 1] = "/"


N, M = map(int, input().split(" "))
grid = [list(input()) for _ in range(3 * N)]
for x, y in product(range(M), range(N)):
    score_operation(grid, 8 * x, 3 * y)
for v in grid:
    print(*v, sep="")
