from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop, heapify
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    x_min, x_max, y_min, y_max = INF, -INF, INF, -INF
    for hh in range(t):
        n, r = (int(input()) for _ in range(2))
        grid = [[int(input()) for _ in range(2 ** n)] for _ in range(2 ** n)]
        operations = [(int(input()), int(input())) for _ in range(r)]
        for op, arg in operations:
            match op:
                case 1:
                    grid = [[grid[y1 * 2 ** arg + (2 ** arg - 1 - y2)][x1 * 2 ** arg + x2] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 2:
                    grid = [[grid[y1 * 2 ** arg + y2][x1 * 2 ** arg + (2 ** arg - 1 - x2)] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 3:
                    grid = [[grid[y1 * 2 ** arg + (2 ** arg - 1 - x2)][x1 * 2 ** arg + y2] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 4:
                    grid = [[grid[y1 * 2 ** arg + x2][x1 * 2 ** arg + (2 ** arg - 1 - y2)] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 5:
                    grid = [[grid[(2 ** (n - arg) - 1 - y1) * 2 ** arg + y2][x1 * 2 ** arg + x2] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 6:
                    grid = [[grid[y1 * 2 ** arg + y2][(2 ** (n - arg) - 1 - x1) * 2 ** arg + x2] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 7:
                    grid = [[grid[(2 ** (n - arg) - 1 - x1) * 2 ** arg + y2][y1 * 2 ** arg + x2] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
                case 8:
                    grid = [[grid[x1 * 2 ** arg + y2][(2 ** (n - arg) - 1 - y1) * 2 ** arg + x2] for x1, x2 in
                             product(range(2 ** (n - arg)), range(2 ** arg))] for y1, y2 in
                            product(range(2 ** (n - arg)), range(2 ** arg))]
        answer = "\n".join(" ".join(map(str, v)) for v in grid)
        answers.append(f"{answer}")
print(*answers, sep="\n")