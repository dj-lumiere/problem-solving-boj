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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        m = int(input())
        grid = [list(map(int, input())) for _ in range(n)]
        answer = 0
        for (i1, i2), (j1, j2) in product(zip(range(n), range(1, n)), zip(range(m), range(1, m))):
            if grid[i1][j1] == grid[i2][j1] == grid[i1][j2] == grid[i2][j2] == 1:
                answer = 1
                break
        answers.append(answer)
    print(*answers, sep="\n")