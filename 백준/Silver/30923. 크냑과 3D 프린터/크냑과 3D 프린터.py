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
        n = int(input())
        heights = [0] + [int(input()) for _ in range(n)]
        answer = 2 * n + sum(heights) * 4
        for i, v in enumerate(heights):
            if i == 0:
                continue
            answer -= min(v, heights[i - 1]) * 2
        answers[h] = f"{answer}"
    print(answers)