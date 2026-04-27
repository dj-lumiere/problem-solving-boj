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
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        _ = int(input())
        number = input().decode()
        result = [0 for _ in range(3)]
        result[0] = int(number, base=8) if all(0<=int(i)<=7 for i in number) else 0
        result[1] = int(number)
        result[2] = int(number, base=16)
        answer = f"{h + 1} {' '.join(map(str, result))}"
        answers[h] = f"{answer}"
    print(answers)