from collections import Counter
from decimal import Decimal, getcontext
from math import gcd
from random import randint
from sys import setrecursionlimit, stdout, stderr

getcontext().prec = 90

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    sqrt_337 = Decimal(337).sqrt()
    answers = []
    for hh in range(t):
        d = Decimal(input())
        h_res = int(input())
        v_res = int(input())
        if d == 0 and h_res == 0 and v_res == 0:
            break
        w = 16 * d / Decimal(sqrt_337)
        h = 9 * d / Decimal(sqrt_337)
        h_dpi = h_res / w
        v_dpi = v_res / h
        answer = f"Horizontal DPI: {h_dpi:.2f}\nVertical DPI: {v_dpi:.2f}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
