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
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        frequencies = sorted(Counter(a).most_common(), key=lambda x: (-x[1], x[0]), )
        answer = frequencies[0][0]
        answers[h] = f"{answer}"
    print(answers)