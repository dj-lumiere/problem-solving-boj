import os
from bisect import bisect_left
from math import pi, sqrt

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        answers[i] = f"{i+1}: {n} {sum(i*(i+1)//2 for i in range(1, n+1))}"
    print(answers)