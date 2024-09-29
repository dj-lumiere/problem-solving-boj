from bisect import bisect_right
from collections import Counter, deque
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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        wires = []
        for _ in range(N):
            Ai = int(input())
            Bi = int(input())
            wires.append((Ai, Bi))
        result = 0
        for i in range(len(wires)):
            for j in range(i + 1, len(wires)):
                if (wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]) or (
                        wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]):
                    result += 1
        answers.append(f"Case #{hh}: {result}")
    print(*answers, sep="\n")