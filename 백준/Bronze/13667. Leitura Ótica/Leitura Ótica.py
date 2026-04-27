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
        answer_sub = ["" for _ in range(n)]
        for h in range(n):
            marks = [int(input()) for _ in range(5)]
            answer = "*"
            answer_count = sum(i <= 127 for i in marks)
            if answer_count == 1:
                index = [i for i, v in enumerate(marks) if v <= 127][0]
                answer = chr(ord('A') + index)
            answer_sub[h] = answer
        answers.append("\n".join(answer_sub))
    print(answers)