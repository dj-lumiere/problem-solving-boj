import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial
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
        answer = f"{n * (n - 1) // 2}\n" + " ".join(map(str, [1 << i for i in
                                                              range(n)])) + f"\n{n - 1}\n" + " ".join(map(str, [
            1 * i + 1 for i in range(n)]))
        answers[h] = f"{answer}"
    print(answers)