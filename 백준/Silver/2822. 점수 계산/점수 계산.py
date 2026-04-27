import os
import re
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
        scores = [-1] + [int(input()) for _ in range(8)]
        scores_sorted = sorted(scores, reverse=True)[:5]
        answer1 = sum(scores_sorted)
        answer2 = [scores.index(i) for i in scores_sorted]
        answer2.sort()
        answer = f"{answer1}\n{' '.join(map(str, answer2))}"
        answers[h] = f"{answer}"
    print(answers)