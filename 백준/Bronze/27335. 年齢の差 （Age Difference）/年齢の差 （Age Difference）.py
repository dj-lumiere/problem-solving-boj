import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial

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
        ages = [int(input()) for _ in range(n)]
        age_sorted = sorted(ages)
        result = [0 for _ in range(n)]
        for i, age in enumerate(ages):
            result[i] = max(abs(age - age_sorted[0]), abs(age - age_sorted[-1]))
        answer = "\n".join(map(str, result))
        answers[h] = answer
    print(answers)