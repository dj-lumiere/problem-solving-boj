import os
from math import comb, factorial

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
        n, a, b, c = [int(input()) for _ in range(4)]
        duplicates = len([a, b, c]) - len({a, b, c}) + 1
        answers[h] = f"{factorial(n) // factorial(a) // factorial(b) // factorial(c)}"
    print(answers)