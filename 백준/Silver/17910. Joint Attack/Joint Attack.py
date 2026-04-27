import os
from fractions import Fraction

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
        x = [int(input()) for _ in range(n)]
        x.reverse()
        answer = Fraction(x[0])
        for i in x[1:]:
            answer = 1 / answer + i
        answers[h] = f"{answer.numerator}/{answer.denominator}"
    print(answers)