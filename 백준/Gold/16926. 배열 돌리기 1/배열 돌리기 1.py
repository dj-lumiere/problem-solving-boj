from itertools import pairwise, permutations
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


    def rotate_grid(grid, r, c, rotation_count):
        new_grid = [v[:] for v in grid]
        for h in range(min(r, c) // 2):
            current_circle = [(i, h) for i in range(h, r - h)]
            current_circle += [(r - h - 1, i) for i in range(h + 1, c - h)]
            current_circle += reversed([(i, c - h - 1) for i in range(h + 1, r - h - 1)])
            current_circle += reversed([(h, i) for i in range(h, c - h)])
            current_circle.reverse()
            current_circle.pop()
            cycle_length = len(current_circle)
            current_circle += current_circle
            rotation_residue = rotation_count % cycle_length
            for (y1, x1), (y2, x2) in zip(current_circle[:cycle_length], current_circle[rotation_residue:]):
                new_grid[y1][x1] = grid[y2][x2]
        return new_grid


    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    t = 1
    for hh in range(t):
        n, m, r = (int(input()) for _ in range(3))
        grid = [[int(input()) for _ in range(m)] for _ in range(n)]
        grid = rotate_grid(grid, n, m, r)
        answer = "\n".join(" ".join(map(str, v)) for v in grid)
        answers.append(f"{answer}")
    print(*answers)