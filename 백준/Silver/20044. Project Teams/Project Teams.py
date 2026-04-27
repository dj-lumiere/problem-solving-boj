import os
from itertools import product
from fractions import Fraction


def is_inbound(x_pos, y_pos, width, height):
    return 0 <= x_pos < width and 0 <= y_pos < height


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        a = [int(input()) for _ in range(2 * n)]
        a.sort()
        answer = min(a[i] + a[-i - 1] for i in range(n))
        answers[h] = f"{answer}"
        print(answers)