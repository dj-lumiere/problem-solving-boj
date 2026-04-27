import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial
import re

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
        formula = input().decode().strip()
        elements = re.split("(C|H|N|O)", formula)
        element_count = {i: 0 for i in "CHNO"}
        recent_element = ""
        for i, v in enumerate(elements):
            if v in list("CHNO"):
                recent_element = v
                continue
            if not recent_element:
                continue
            if v == '':
                element_count[recent_element] += 1
            else:
                element_count[recent_element] += int(v)
        answer = 0.0
        for element, count in element_count.items():
            if element == "C":
                answer += count * 12.01
            if element == "H":
                answer += count * 1.008
            if element == "O":
                answer += count * 16.00
            if element == "N":
                answer += count * 14.01
        answers[h] = f"{answer:.3f}"
    print(answers)