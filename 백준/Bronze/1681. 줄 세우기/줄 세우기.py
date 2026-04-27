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
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        l = int(input())
        answer = 0
        can_be_labeled = []
        for i in range(1, 3000000):
            if str(l) in str(i):
                continue
            can_be_labeled.append(i)
            if len(can_be_labeled) == n:
                break
        eprint(len(can_be_labeled))
        answer = can_be_labeled[n - 1]
        answers[h] = f"{answer}"
    print(answers)