import os
from collections import Counter
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        grid = [[int(input()) for _ in range(n * n)] for _ in range(n * n)]
        answers[h] = "CORRECT" if (
            all(all(m == 1 for m in Counter([grid[(i // n) * n + j // n][(i % n) * n + j % n] for j in range(n * n) if grid[(i // n) * n + j // n][(i % n) * n + j % n]]).values()) for i in range(n * n))
        and all(all(m == 1 for m in Counter([grid[i][j] for j in range(n * n) if grid[i][j]]).values()) for i in range(n * n))
        and all(all(m == 1 for m in Counter([grid[j][i] for j in range(n * n) if grid[j][i]]).values()) for i in range(n * n))
        ) else "INCORRECT"
    print(answers)