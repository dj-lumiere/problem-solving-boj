import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        a = [input().decode() for _ in range(n)]
        answer = ["" for _ in range(n)]
        for i in range((n + 1) // 2):
            answer[2 * i] = a[i]
            if 2 * i + 1 == n:
                continue
            answer[2 * i + 1] = a[(n + 1) // 2 + i]
        answers.append("\n".join(answer))
    print(answers)