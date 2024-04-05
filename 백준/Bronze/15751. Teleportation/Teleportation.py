import os
from itertools import permutations

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        a, b, x, y = [int(input()) for _ in range(4)]
        a, b = min(a, b), max(a, b)
        x, y = min(x, y), max(x, y)
        answers[i] = str(min(b - a, abs(a - x) + abs(b - y)))
    print(answers)