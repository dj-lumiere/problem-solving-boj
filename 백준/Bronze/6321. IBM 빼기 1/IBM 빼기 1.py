import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        word = input().decode()
        answer = "".join(chr((ord(i) - ord('A') + 1) % 26 + ord('A')) for i in word)
        answers[h] = f"String #{h + 1}\n{answer}"
    print(answers)