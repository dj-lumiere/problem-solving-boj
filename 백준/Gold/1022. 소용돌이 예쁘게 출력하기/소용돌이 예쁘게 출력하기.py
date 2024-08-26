from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop, heapify
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain
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
    DELTA = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        r1, c1, r2, c2 = [int(input()) for _ in range(4)]
        new_grid = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
        if r1 <= 0 <= r2 and c1 <= 0 <= c2:
            r, c = 0, 0
            new_grid[r - r1][c - c1] = 1
        if r1 <= 0 <= r2 and c1 <= 1 <= c2:
            r, c = 0, 1
            new_grid[r - r1][c - c1] = 2
        start = [1, 0]  # (x, y)
        current_number = 2
        for i in range(5000):
            current_orbit = 2 * i + 2
            for (j, (dx, dy)), k in product(enumerate(DELTA), range(current_orbit)):
                if j == 0 and k == 1:
                    continue
                x, y = start
                nx, ny = x + dx, y + dy
                current_number += 1
                if r1 <= ny <= r2 and c1 <= nx <= c2:
                    r, c = ny, nx
                    new_grid[r - r1][c - c1] = current_number
                start = [nx, ny]
            else:
                if i != 5000:
                    dx, dy = DELTA[-1]
                    x, y = start
                    nx, ny = x + dx, y + dy
                    current_number += 1
                    if r1 <= ny <= r2 and c1 <= nx <= c2:
                        r, c = ny, nx
                        new_grid[r - r1][c - c1] = current_number
                    start = [nx, ny]
        max_digit = max(max(len(str(v2)) for v2 in v) for v in new_grid)
        answer = "\n".join(" ".join(map(lambda x: str(x).rjust(max_digit, " "), v)) for v in new_grid)
        answers.append(f"{answer}")
print(*answers, sep="\n")