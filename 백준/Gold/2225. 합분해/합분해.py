from itertools import product
from sys import stdout, stderr

with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    grid = [[0 for n in range(201)] for k in range(201)]
    for k, n in product(range(201), repeat=2):
        if k == 0:
            continue
        if k == 1:
            grid[k][n] = 1
            continue
        for i in range(n + 1):
            grid[k][n] += grid[k - 1][i]
        grid[k][n] %= MOD
    for hh in range(t):
        n, k = map(int, input().split())
        answer = grid[k][n]
        answers.append(f"{answer}")
    print(*answers, sep="\n")
