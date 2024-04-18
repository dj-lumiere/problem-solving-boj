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
        a, b = map(int, input().decode().split("/"))
        answer = Fraction(a, b).limit_denominator(b - 1)
        answers[h] = f"{answer.numerator}/{answer.denominator}"
    print(answers)