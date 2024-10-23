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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        v = int(input())
        answer = INF
        for a in range(1, int(v ** (1/3)) + 2):
            if v % a == 0:
                for b in range(a, int((v // a) ** 0.5) + 1):
                    if (v // a) % b == 0:
                        c = v // (a * b)
                        answer = min(answer, 2 * (a * b + b * c + c * a))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
