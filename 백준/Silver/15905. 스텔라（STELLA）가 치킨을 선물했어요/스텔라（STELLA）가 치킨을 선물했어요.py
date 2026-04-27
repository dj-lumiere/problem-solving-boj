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
        solve_penalty = [(int(input()), int(input())) for _ in range(n)]
        solve_penalty.sort(key=lambda x: (-x[0], x[1]))
        fifth_solves = solve_penalty[4][0]
        fifth_penalty = solve_penalty[4][1]
        answer = 0
        for i, j in solve_penalty:
            if i == fifth_solves and j > fifth_penalty:
                answer += 1
        answers[h] = f"{answer}"
    print(answers)