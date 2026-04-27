import os
from collections import Counter
from itertools import combinations, permutations, product
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
        a = [int(input()) for _ in range(3)]
        b = [int(input()) for _ in range(3)]
        answer = max(a1*b[0]+a2*b[1]+a3*b[2] for a1, a2, a3 in permutations(a))
        answers[h] = f"{answer}"
    print(answers)