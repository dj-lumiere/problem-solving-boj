import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        n = list(map(int, input().split()))
        answer = "Good"
        for i, v in enumerate(n):
            if i == 0:
                continue
            if n[i-1] > v:
                answer = "Bad"
                break
        answers[h] = f"{answer}"
    print(answers)