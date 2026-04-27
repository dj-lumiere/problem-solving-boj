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
        d1, m1, y1, n = [int(input()) for _ in range(4)]
        d2, m2, y2 = [int(input()) for _ in range(3)]
        answer = ((y2 - y1) * 360 + (m2 - m1) * 30 + d2 - d1 + n - 1) % 7 + 1
        answers[h] = f"{answer}"
    print(answers)