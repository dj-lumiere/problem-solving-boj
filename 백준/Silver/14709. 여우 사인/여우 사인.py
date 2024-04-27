import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial, log, sin
import re

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
        finger = [tuple(sorted([int(input()) for _ in range(2)])) for _ in range(n)]
        if all(i in [(1, 3), (1, 4), (3, 4)] for i in finger) and n >= 3:
            answer = "Wa-pa-pa-pa-pa-pa-pow!"
        else:
            answer = "Woof-meow-tweet-squeek"
        answers[h] = f"{answer}"
    print(answers)