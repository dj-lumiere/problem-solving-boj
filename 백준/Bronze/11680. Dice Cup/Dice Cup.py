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
        m = int(input())
        frequencies = Counter(i + j for i, j in product(range(1, n + 1), range(1, m + 1)))
        most_frequent = max(frequencies.values())
        answer = [i for i, j in frequencies.items() if j == most_frequent]
        answer.sort()
        answers[h] = "\n".join(map(str, answer))
    print(answers)