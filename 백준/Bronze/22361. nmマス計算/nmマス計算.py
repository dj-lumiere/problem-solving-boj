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
    while True:
        n = int(input())
        m = int(input())
        if n == m == 0:
            break
        number_count = [0 for _ in range(10)]
        a = [int(input()) for _ in range(n)]
        b = [int(input()) for _ in range(m)]
        for i in a:
            for j in b:
                for k in str(i * j):
                    number_count[int(k)] += 1
        answers.append(" ".join(map(str, number_count)))
    print(answers)