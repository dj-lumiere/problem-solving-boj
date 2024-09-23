from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from math import sqrt
from sys import stdout, stderr

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
    t = int(input())
    answers = []
    for hh in range(t):
        a, b, c = (float(input()) for _ in range(3))
        roots = [(-b + i * sqrt(b * b - 4 * a * c)) / (2 * a) for i in reversed(range(-1, 2, 2))]
        answer = ", ".join([f"{i:.3f}" for i in roots])
        answers.append(f"{answer}")
    print(*answers, sep="\n")