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
    pattern = input().decode()
    asterisk = pattern.index("*")
    start = pattern[:asterisk]
    end = pattern[asterisk+1:]
    eprint((start, end))
    answers = ["" for _ in range(t)]
    for h in range(t):
        word = input().decode()
        answer = "NE"
        if word.startswith(start) and word.endswith(end) and len(word) >= len(start)+len(end):
            answer = "DA"
        answers[h] = f"{answer}"
    print(answers)