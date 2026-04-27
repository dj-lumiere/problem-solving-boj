import os
from itertools import product
from fractions import Fraction

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
        l = int(input())
        d = int(input())
        x = int(input())
        n = d
        m = l
        for i in range(l, d+1):
            digit_sum = sum([int(j) for j in str(i)])
            if digit_sum == x:
                n = min(i, n)
                m = max(i, m)
        answer = f"{n}\n{m}"
        answers[h] = f"{answer}"
    print(answers)