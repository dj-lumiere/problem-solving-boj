import os
from collections import deque
from copy import deepcopy
from itertools import permutations

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        answer = [(0, 0), 100000.0]
        dots = [(int(input()), int(input())) for _ in range(n)]
        answer[0] = (sum(i for i, j in dots), sum(j for i, j in dots))
        for b in range(n):
            dest = (sum(i for a, (i, j) in enumerate(dots) if a != b), sum(j for a, (i, j) in enumerate(dots) if a != b))
            if answer[1] > (dest[0] ** 2 + dest[1] ** 2) ** .5:
                answer[1] = (dest[0] ** 2 + dest[1] ** 2) ** .5
        answers[h] = f"{answer[0][0]} {answer[0][1]}\n{answer[1]:.2f}"
    print(answers)