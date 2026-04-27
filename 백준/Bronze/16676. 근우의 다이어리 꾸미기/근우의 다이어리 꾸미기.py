import os
from collections import Counter
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        digit = len(str(n))
        answer = digit
        if 10**(digit-1) <= n < int("1"*digit):
            answer -= 1
        answers[h] = f"{answer}"
    print(answers)