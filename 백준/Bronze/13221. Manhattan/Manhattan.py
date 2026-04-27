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
        you = (int(input()), int(input()))
        a,b = you
        n = int(input())
        taxies = [(int(input()), int(input())) for _ in range(n)]
        distance = [abs(a-x)+abs(b-y) for x,y in taxies]
        answer = taxies[distance.index(min(distance))]
        answers[h] = f"{answer[0]} {answer[1]}"
    print(answers)