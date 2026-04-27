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
        a = [input().decode() for _ in range(n)]
        a2 = [("BSGPD".index(i[0])) * 10000 - int(i[1:]) + 10000 for i in a]
        a2_sorted = sorted(a2)
        changes = [i for i, j in zip(a2, a2_sorted) if i != j]
        changes.sort()
        if changes:
            tier1, remainder1 = divmod(changes[0], 10000)
            tier2, remainder2 = divmod(changes[1], 10000)
            answer = f"KO\n{'BSGPD'[tier1]}{10000 - remainder1} {'BSGPD'[tier2]}{10000 - remainder2}"
        else:
            answer = "OK"
        answers[h] = f"{answer}"
    print(answers)