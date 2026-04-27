import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        a = {int(input()) for _ in range(n)}
        m = int(input())
        b = [int(input()) for _ in range(m)]
        answer = [int(i in a) for i in b]
        answers[h] = "\n".join(map(str, answer))
    print(answers)