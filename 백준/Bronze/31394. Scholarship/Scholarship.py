from bisect import bisect_right
from collections import deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from operator import index
from sys import stdout, stderr
from itertools import permutations

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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        marks = [int(input()) for _ in range(n)]
        has_satisfactory = any(mark == 3 for mark in marks)
        average_mark = sum(marks) / n
        if all(mark == 5 for mark in marks):
            answer = "Named"
        elif not has_satisfactory and average_mark >= 4.5:
            answer = "High"
        elif not has_satisfactory:
            answer = "Common"
        else:
            answer = "None"
        answers.append(answer)
    print(*answers, sep="\n")