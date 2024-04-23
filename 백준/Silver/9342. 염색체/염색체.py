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
    t = int(input())
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        n = input().decode()
        answer = "Infected!"
        if n[0] not in "ABCDEF":
            answer = "Good"
        if n[-1] not in "ABCDEF":
            answer = "Good"
        uniques1 = []
        for i, v in enumerate(n[1:-1]):
            if not uniques1:
                uniques1.append(v)
                continue
            if uniques1[-1] != v:
                uniques1.append(v)
        uniques2 = []
        for i, v in enumerate(n[1:]):
            if not uniques2:
                uniques2.append(v)
                continue
            if uniques2[-1] != v:
                uniques2.append(v)
        uniques3 = []
        for i, v in enumerate(n[:-1]):
            if not uniques3:
                uniques3.append(v)
                continue
            if uniques3[-1] != v:
                uniques3.append(v)
        uniques4 = []
        for i, v in enumerate(n[:]):
            if not uniques4:
                uniques4.append(v)
                continue
            if uniques4[-1] != v:
                uniques4.append(v)
        if not any(i == ["A", "F", "C"] for i in [uniques1, uniques2, uniques3, uniques4]):
            answer = "Good"
        answers[h] = f"{answer}"
    print(answers)