from itertools import permutations
from os import write
from sys import stdout, stderr

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    print = lambda *args, sep=" ", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    answers = []


    def input():
        try:
            return next(tokens)
        except StopIteration:
            return None


    def rotate_grid(grid, n, m, r, c, s):
        new_grid = [v[:] for v in grid]
        for h in range(1, s + 1):
            current_circle = [(r - h, i) for i in range(c - h, c + h + 1)]
            current_circle += [(i, c + h) for i in range(r - h + 1, r + h + 1)]
            current_circle += reversed([(r + h, i) for i in range(c - h, c + h)])
            current_circle += reversed([(i, c - h) for i in range(r - h, r + h)])
            for (y1, x1), (y2, x2) in zip(current_circle, current_circle[1:]):
                new_grid[y2][x2] = grid[y1][x1]
        return new_grid


    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    t = 1
    for hh in range(t):
        n, m, k = (int(input()) for _ in range(3))
        grid = [[0 for _ in range(m + 1)]] + [[0] + [int(input()) for _ in range(m)] for _ in range(n)]
        operations = [[int(input()) for _ in range(3)] for _ in range(k)]
        value_min = INF
        for ops in permutations(operations):
            new_grid = [v[:] for v in grid]
            for r, c, s in ops:
                new_grid = rotate_grid(new_grid, n, m, r, c, s)
            value_min = min(min(sum(v) for v in new_grid[1:]), value_min)
        answer = value_min
        answers.append(f"{answer}")
    print(*answers)
