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
        b = int(input())
        heights = [int(input()) for _ in range(n)]
        total_heights = []
        for i in range(1, 2 ** n):
            contain = [i & (1 << j) != 0 for j in range(n)]
            stack_height = sum(j * k for j, k in zip(contain, heights))
            if stack_height < b:
                continue
            total_heights.append((stack_height, sum(contain)))
        eprint(total_heights)
        total_heights.sort(key=lambda x: (x[0], x[1]))
        answer = total_heights[0][0] - b
        answers[h] = f"{answer}"
    print(answers)