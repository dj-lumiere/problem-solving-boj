from bisect import bisect_left, bisect_right
from collections import Counter, deque
from decimal import getcontext
from itertools import combinations, product
from math import floor, log10
from sys import stdout, stderr
from fractions import Fraction

getcontext().prec = 1000

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
    t = 1
    answers = []
    for hh in range(t):
        n, m = int(input()), int(input())
        dots = [int(input()) for _ in range(n)]
        dots.sort()
        for _ in range(m):
            a, b = int(input()), int(input())
            answer = bisect_right(dots, b)-bisect_left(dots, a)
            answers.append(f"{answer}")
    print(*answers, sep="\n")