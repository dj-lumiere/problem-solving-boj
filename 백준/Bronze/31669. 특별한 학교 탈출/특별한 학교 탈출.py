from collections import deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
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
        N, M = (int(input()) for _ in range(2))
        patrol_schedule = [list(input()) for _ in range(N)]
        answer = "ESCAPE FAILED"
        for period in range(M):
            if all(patrol_schedule[teacher][period] == "X" for teacher in range(N)):
                answer = f"{period + 1}"
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")