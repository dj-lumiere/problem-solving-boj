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
    t = int(input())
    answers = ["" for _ in range(t)]
    fibs = [1, 2]
    for _ in range(20):
        fibs.append(fibs[-1] + fibs[-2])
    for h in range(t):
        n = int(input())
        answer_bit = [False for _ in range(22)]
        for i, v in enumerate(reversed(fibs), start=1):
            if n >= v:
                n -= v
                answer_bit[-i] = True
        answer = sum(fibs[i] * v for i, v in enumerate(answer_bit[1:]))
        answers[h] = f"{answer}"
    print(answers)