import os
from collections import Counter
from itertools import combinations, product
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
        n, l, d = [int(input()) for _ in range(3)]
        can_be_answered = ([False] * l + [True] * 5) * n + [True] * 1000
        answer = 0
        for i in range(len(can_be_answered)):
            if i % d == 0 and can_be_answered[i]:
                answer = i
                break
        answers[h] = f"{answer}"
    print(answers)