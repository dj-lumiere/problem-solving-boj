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
    t = INF
    answers = []
    for hh in range(t):
        n = list(input())
        if n == ["#"]:
            break
        answer = "not possible"
        for i, v in enumerate(n):
            n2 = n[:]
            n2.pop(i)
            if n2 == n2[::-1]:
                answer = "".join(n2)
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")