import os
from math import ceil, floor, log2

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        a, b = int(input()), int(input())
        answer = (a // b) ** 2
        answers[h] = f"{answer}"
    print(answers)