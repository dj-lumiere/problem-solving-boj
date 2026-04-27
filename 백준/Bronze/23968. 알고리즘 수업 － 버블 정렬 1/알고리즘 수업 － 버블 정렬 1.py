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
        k = int(input())
        a = [0] + [int(input()) for _ in range(n)]
        last_change = [0, 0]
        for last in range(n, 1, -1):
            for i in range(1, last):
                if a[i] > a[i + 1]:
                    if k > 0:
                        a[i], a[i + 1] = a[i + 1], a[i]
                        last_change = [a[i + 1], a[i]]
                        k -= 1
        if k > 0:
            answer = "-1"
        else:
            last_change.sort()
            answer = f"{last_change[0]} {last_change[1]}"
        answers[h] = f"{answer}"
    print(answers)