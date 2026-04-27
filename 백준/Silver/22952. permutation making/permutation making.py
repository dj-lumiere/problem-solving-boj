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
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        answer = [0 for _ in range(n)]
        for i, v in enumerate(range(1, n // 2 + 1)):
            answer[2 * i] = v
            answer[2 * i + 1] = n - v
        answer[n - 1] = n
        answers[h] = " ".join(map(str, answer))
    print(answers)