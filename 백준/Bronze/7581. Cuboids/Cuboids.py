from decimal import getcontext
from itertools import product
from sys import stderr, stdout

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(1, t + 1):
        a, b, c, d = (int(input()) for _ in range(4))
        if a == b == c == d == 0:
            break
        if a == 0:
            a = d // b // c
        if b == 0:
            b = d // a // c
        if c == 0:
            c = d // a // b
        if d == 0:
            d = a * b * c
        answer = f"{a} {b} {c} {d}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")