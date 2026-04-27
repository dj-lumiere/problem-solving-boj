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
        a = [int(input()) for _ in range(6)]
        b = [int(input()) for _ in range(6)]
        answer = Fraction(sum(i>j for i, j in product(a, b)), 36)
        answers[h] = f"{answer.numerator}/{answer.denominator}"
    print(answers)