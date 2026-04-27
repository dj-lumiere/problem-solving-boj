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
        m = int(input())
        adjectives = [input().decode() for _ in range(n)]
        nouns = [input().decode() for _ in range(m)]
        answer = [f"{i} as {j}" for i, j in product(adjectives, nouns)]
        answers[h] = "\n".join(answer)
    print(answers)