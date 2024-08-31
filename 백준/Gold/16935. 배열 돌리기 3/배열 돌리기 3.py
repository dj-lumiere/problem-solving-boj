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
        n, m, r = (int(input()) for _ in range(3))
        grid = [[int(input()) for _ in range(m)] for _ in range(n)]
        operations = [int(input()) for _ in range(r)]
        for op in operations:
            match op:
                case 1:
                    grid = [[grid[-y - 1][x] for x in range(m)] for y in range(n)]
                case 2:
                    grid = [[grid[y][-x - 1] for x in range(m)] for y in range(n)]
                case 3:
                    grid = [[grid[-x - 1][y] for x in range(n)] for y in range(m)]
                    n, m = m, n
                case 4:
                    grid = [[grid[x][-y - 1] for x in range(n)] for y in range(m)]
                    n, m = m, n
                case 5:
                    grid = [[grid[(1 - x1) * (n // 2) + y2][y1 * (m // 2) + x2] for x1, x2 in
                             product(range(2), range(m // 2))] for y1, y2 in product(range(2), range(n // 2))]
                case 6:
                    grid = [[grid[x1 * (n // 2) + y2][(1 - y1) * (m // 2) + x2] for x1, x2 in
                             product(range(2), range(m // 2))] for y1, y2 in product(range(2), range(n // 2))]
        answer = "\n".join(" ".join(map(str, v)) for v in grid)
        answers.append(f"{answer}")
    print(*answers, sep="\n")