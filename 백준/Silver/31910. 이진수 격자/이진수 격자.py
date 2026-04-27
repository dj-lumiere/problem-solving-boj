from os import write
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for r, c in product(range(n), repeat=2):
            if r == c == 0:
                dp[r][c] = grid[r][c]
            elif r == 0:
                dp[r][c] = dp[r][c-1]*2+grid[r][c]
            elif c == 0:
                dp[r][c] = dp[r-1][c]*2+grid[r][c]
            else:
                dp[r][c] = max(dp[r][c-1]*2+grid[r][c], dp[r-1][c]*2+grid[r][c])
        answer = dp[-1][-1]
        answers.append(f"{answer}")
    print(answers)