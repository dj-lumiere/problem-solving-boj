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
    t = 0
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        pass
    x = [0 for _ in range(1000001)]
    x[0] = 1
    for i in range(1, 1000001):
        x[i] = (x[int(i - i ** .5)] + x[int(log(i))] + x[int(i * sin(i) * sin(i))]) % 1_000_000
    while True:
        n = int(input())
        if n == -1:
            break
        answers.append(f"{x[n]}")
    print(answers)