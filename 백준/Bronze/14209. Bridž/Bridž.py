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
        a = [input().decode() for _ in range(n)]
        card_points = ["X", "J", "Q", "K", "A"]
        answer = 0
        for i in a:
            answer += sum(card_points.index(j) for j in i)
        answers[h] = f"{answer}"
    print(answers)