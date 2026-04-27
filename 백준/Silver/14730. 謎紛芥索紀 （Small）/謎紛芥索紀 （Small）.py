import os
from collections import deque
from copy import deepcopy

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
        answer = 0
        for _ in range(n):
            a, b = int(input()), int(input())
            answer += a * b
        answers[h] = f"{answer}"
    print(answers)