import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial, log, sin
import re

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        n = int(input())
        k = [int(input()) for _ in range(n)]
        a = [int(input()) for _ in range(n)]
        b = [int(input()) for _ in range(n)]
        answer = [sorted([ki, ai, bi])[1] for ki, ai, bi in zip(k, a, b)]
        answers[h] = " ".join(map(str, answer))
    print(answers)