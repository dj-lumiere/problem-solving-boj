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
        date_raw = input().decode()
        eprint(date_raw)
        answer = ""
        if "." in date_raw:
            day, month, year = map(int, date_raw.split("."))
            answer = f"{day:0>2}.{month:0>2}.{year:0>4} {month:0>2}/{day:0>2}/{year:0>4}"
        elif "/" in date_raw:
            month, day, year = map(int, date_raw.split("/"))
            answer = f"{day:0>2}.{month:0>2}.{year:0>4} {month:0>2}/{day:0>2}/{year:0>4}"
        answers[h] = f"{answer}"
    print(answers)