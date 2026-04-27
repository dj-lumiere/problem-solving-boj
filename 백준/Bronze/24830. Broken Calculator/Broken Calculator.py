import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        a, op, b = input().decode().split()
        a = int(a)
        b = int(b)
        if op == "+":
            prev_answer = a + b - prev_answer
        if op == "-":
            prev_answer = (a - b) * prev_answer
        if op == "*":
            prev_answer = a * b * a * b
        if op == "/":
            if a % 2 == 0:
                prev_answer = a // 2
            else:
                prev_answer = (a + 1) // 2
        answers[h] = f"{prev_answer}"
    print(answers)