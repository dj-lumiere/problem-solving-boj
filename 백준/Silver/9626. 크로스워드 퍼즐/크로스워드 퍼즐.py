from itertools import product
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        m, n = int(input()), int(input())
        u, l, r, d = (int(input()) for _ in range(4))
        grid = [["." if (i + j) & 1 else "#" for j in range(l + r + n)] for i in range(u + d + m)]
        words = [input() for _ in range(m)]
        for i, j in product(range(u, u + m), range(l, l + n)):
            grid[i][j] = words[i - u][j - l]
        answer = "\n".join("".join(x) for x in grid)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
