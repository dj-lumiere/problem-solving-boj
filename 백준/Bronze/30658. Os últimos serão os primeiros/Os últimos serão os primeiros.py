import os
from math import gcd, log2, ceil

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    # for i in range(t):
    #     w = int(input())
    #     l = int(input())
    #     h = int(input())
    #     wl_min, wl_max = min(w, l), max(w, l)
    #     if wl_min >= h * 2 and wl_max <= wl_min * 2:
    #         answers[i] = "good"
    #     else:
    #         answers[i] = "bad"
    while True:
        n = int(input())
        if n == 0:
            break
        a = [int(input()) for _ in range(n)]
        answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)