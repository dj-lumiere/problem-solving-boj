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
        m = int(input())
        a = [int(input()) for _ in range(n)]
        b = [0]
        for v in a:
            b.append(b[-1] + v)
        answer = 0
        for i, j in product(range(n + 1), repeat=2):
            if i >= j:
                continue
            if b[j] - b[i] == m:
                answer += 1
        answers[h] = f"{answer}"
    print(answers)