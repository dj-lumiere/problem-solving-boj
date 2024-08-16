from itertools import product
from sys import stdout, stderr

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
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        sums = ([sum(grid[i][j] for j in range(n)) for i in range(n)]
                + [sum(grid[j][i] for j in range(n)) for i in range(n)]
                + [sum(grid[i][i] for i in range(n)), sum(grid[i][-i - 1] for i in range(n))])
        answer = "TRUE"
        if not all(i == n * (n ** 2 + 1) // 2 for i in sums):
            answer = "FALSE"
        if not all(1 <= grid[i][j] <= n ** 2 for i, j in product(range(n), repeat=2)):
            answer = "FALSE"
        if len(set(grid[i][j] for i, j in product(range(n), repeat=2))) != n ** 2:
            answer = "FALSE"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
