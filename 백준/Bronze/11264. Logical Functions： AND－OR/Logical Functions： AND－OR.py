import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        mode = input().decode()
        w1, w2, b = [float(input()) for _ in range(3)]
        inputs = [(1,1), (1,0), (0,1), (0,0)]
        and_out = [1,0,0,0]
        or_out = [1,1,1,0]
        output = [int(w1*i+w2*j+b>=0.0) for i,j in inputs]
        correct = and_out if mode == "AND" else or_out
        answer = "true" if correct==output else "false"
        answers[h] = f"{answer}"
    print(answers)