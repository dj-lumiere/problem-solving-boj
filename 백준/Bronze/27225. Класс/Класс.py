import os
from collections import Counter, deque
from itertools import product
from array import array
from functools import reduce
from datetime import date, timedelta

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
        m = int(input())
        answer = min(n, m) * 2 + ((n + m) % 2)
        answers[h] = f"{answer}"
    print(answers)