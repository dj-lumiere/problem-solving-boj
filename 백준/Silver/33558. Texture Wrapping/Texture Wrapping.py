from itertools import product
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n, m = (int(input()) for _ in range(2))
        u, v = (int(input()) for _ in range(2))
        texture = [list(input()) for _ in range(u)]
        mode = input()
        grid = [["" for _ in range(m)] for _ in range(n)]
        if mode == "clamp-to-edge":
            for y, x in product(range(n), range(m)):
                grid[y][x] = texture[min(y, u - 1)][min(x, v - 1)]
        if mode == "repeat":
            for y, x in product(range(n), range(m)):
                grid[y][x] = texture[y % u][x % v]
        if mode == "mirrored-repeat":
            for y, x in product(range(n), range(m)):
                y_rev = (y // u) & 1
                x_rev = (x // v) & 1
                eff_y = y % u
                eff_x = x % v
                if y_rev:
                    eff_y = -eff_y - 1
                if x_rev:
                    eff_x = -eff_x - 1
                grid[y][x] = texture[eff_y][eff_x]
        answer = "\n".join("".join(v2) for v2 in grid)
        answers.append(answer)
    print(*answers, sep="\n")