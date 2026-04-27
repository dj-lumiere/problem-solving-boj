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
    t = 0
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        p = int(input(), base=n)
        m = int(input(), base=n)
        answer = p % m
        result = []
        while answer != 0:
            result.append(answer % n)
            answer = answer // n
        if not result:
            result.append(0)
        eprint(result)
        answers.append("".join(map(str, reversed(result))))
    print(answers)