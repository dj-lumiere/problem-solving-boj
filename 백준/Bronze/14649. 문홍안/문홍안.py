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
        l = int(input())
        press_count = [0 for _ in range(100)]
        for _ in range(l):
            x, y = int(input()), input().decode()
            if y == "L":
                for i in range(x - 2, -1, -1):
                    press_count[i] += 1
            if y == "R":
                for i in range(x, 100):
                    press_count[i] += 1
        eprint(press_count)
        ratios = [0, 0, 0]
        for v in press_count:
            ratios[v % 3] += 1
        answer = [n / 100 * ratios[i] for i in range(3)]
        answers[h] = "\n".join(f"{x:.2f}" for x in answer)
    print(answers)