from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        R, C = int(input()), int(input())
        grid = [list(input()) for _ in range(R)]
        A, B = int(input()), int(input())
        full_grid = []
        for i in range(2 * R):
            row = []
            for j in range(2 * C):
                if i < R and j < C:
                    row.append(grid[i][j])
                elif i < R and j >= C:
                    row.append(grid[i][2 * C - j - 1])
                elif i >= R and j < C:
                    row.append(grid[2 * R - i - 1][j])
                else:
                    row.append(grid[2 * R - i - 1][2 * C - j - 1])
            full_grid.append(row)
        A_idx, B_idx = A - 1, B - 1
        full_grid[A_idx][B_idx] = '#' if full_grid[A_idx][B_idx] == '.' else '.'
        answer = '\n'.join(''.join(row) for row in full_grid)
        answers.append(f"{answer}")
    print(*answers, sep="\n")