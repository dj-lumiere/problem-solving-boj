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
        n = int(input())
        # 1+x+xx = n
        answer = []
        for _ in range(n):
            i = int(input())
            if i == 6:
                continue
            answer.append(str(i + 1))
        answers[h] = f"Case {h + 1}:" + ("\n" + "\n".join(answer) if answer else "")
    print(answers)