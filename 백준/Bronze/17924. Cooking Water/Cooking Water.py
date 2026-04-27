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
        n = int(input())
        can_be_boiling = [0 for _ in range(1001)]
        for _ in range(n):
            a, b = int(input()), int(input())
            can_be_boiling[a:(b + 1)] = [i + 1 for i in can_be_boiling[a:(b + 1)]]
        eprint(can_be_boiling)
        answer = max(can_be_boiling)
        answers[h] = "gunilla has a point" if answer == n else "edward is right"
    print(answers)