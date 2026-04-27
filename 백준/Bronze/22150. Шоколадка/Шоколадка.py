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
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        lengths = [int(input()) for _ in range(2 * n)]
        answer = "no" if all(lengths[2 * i] + lengths[2 * i + 1] == n for i in range(n)) else "yes"
        answers[h] = f"{answer}"
    print(answers)