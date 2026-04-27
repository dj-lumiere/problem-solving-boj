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
        _ = int(input())
        n = input().decode()
        north_dist = 0
        east_dist = 0
        for i in n:
            if i == 'N':
                north_dist += 1
            if i == 'S':
                north_dist -= 1
            if i == "E":
                east_dist += 1
            if i == "W":
                east_dist -= 1
        answer = abs(north_dist) + abs(east_dist)
        answers[h] = f"{answer}"
    print(answers)