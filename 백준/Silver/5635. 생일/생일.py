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
    prev_answer = 1
    for h in range(t):
        n = int(input())
        names = [(input().decode(), int(input()), int(input()), int(input())) for _ in range(n)]
        eprint(names)
        names.sort(key=lambda x: (x[3], x[2], x[1]))
        answers[h] = f"{names[-1][0]}\n{names[0][0]}"
    print(answers)