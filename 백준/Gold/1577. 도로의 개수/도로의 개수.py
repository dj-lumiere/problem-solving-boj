from itertools import product
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
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
        n = int(input())
        m = int(input())
        k = int(input())
        roads = {tuple(sorted([tuple(int(input()) for _ in range(2)) for _ in range(2)])) for _ in range(k)}
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = 1
        for r, c in product(range(m + 1), range(n + 1)):
            if r == c == 0:
                continue
            if r == 0:
                if ((c - 1, r), (c, r)) in roads:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r][c - 1]
            elif c == 0:
                if ((c, r - 1), (c, r)) in roads:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c]
            else:
                if ((c, r - 1), (c, r)) not in roads:
                    dp[r][c] += dp[r - 1][c]
                if ((c - 1, r), (c, r)) not in roads:
                    dp[r][c] += dp[r][c - 1]
        result = dp[m][n]
        answer = f"{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
