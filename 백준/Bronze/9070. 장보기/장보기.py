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
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        price = [(int(input()), int(input())) for _ in range(n)]
        price.sort(key=lambda x: (-x[0]/x[1], x[1]))
        answer = price[0][1]
        answers[h] = f"{answer}"
    print(answers)