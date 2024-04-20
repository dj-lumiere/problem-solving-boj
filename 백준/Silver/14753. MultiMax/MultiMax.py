import os
from collections import Counter
from itertools import combinations, product
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
        a = [int(input()) for _ in range(n)]
        a.sort(reverse=True)
        candidates = [a[0]*a[1], a[0]*a[1]*a[2]]
        positives = [i for i in a if i > 0]
        positives.sort(reverse=True)
        negatives = [i for i in a if i < 0]
        negatives.sort()
        if len(negatives) >= 2:
            candidates.append(negatives[0]*negatives[1]*a[0])
            candidates.append(negatives[0]*negatives[1])
        answer = max(candidates)
        answers[h] = f"{answer}"
    print(answers)