import os
from collections import Counter, deque
from itertools import product
from array import array
from functools import reduce

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
        records = [int(input()) for _ in range(n)]
        answer = -1 if not n or all(not i for i in records) else 1
        answers[h] = f"{answer:.2f}" if answer != -1 else "divide by zero"
    print(answers)