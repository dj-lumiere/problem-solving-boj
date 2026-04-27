import os
from collections import Counter
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
        a, b, c, n = [int(input()) for _ in range(4)]
        if a < c:
            answer = 0
        elif (a - c) * n + b >= 0:
            answer = 1
        else:
            answer = 0
        answers[h] = f"{answer}"
    print(answers)