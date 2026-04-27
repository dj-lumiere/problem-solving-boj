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
        ds = int(input())
        ys = int(input())
        dm = int(input())
        ym = int(input())
        answer = 0
        for i in range(1, 5001):
            if (i + ds) % (ys) == (i + dm) % (ym):
                answer = i
                break
        answers[h] = f"{answer}"
    print(answers)