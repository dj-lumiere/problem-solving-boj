import os
from collections import Counter, deque
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
        a, b = int(input()), int(input())
        e = [int(input()) for _ in range(b)]
        fronts = []
        has_been_front = set()
        for v in reversed(e):
            if v not in has_been_front:
                fronts.append(v)
                has_been_front.add(v)
        answer = fronts + [i for i in range(1, a + 1) if i not in has_been_front]
        answers[h] = "\n".join(map(str, answer))
    print(answers)