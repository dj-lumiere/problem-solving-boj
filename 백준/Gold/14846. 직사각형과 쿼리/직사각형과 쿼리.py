from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import stdout, stderr, setrecursionlimit
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, \
    zip_longest, chain
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from array import array
import re

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
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        counts = [[[0 for _ in range(11)] for _ in range(n + 1)] for _ in range(n + 1)]
        for r, c in product(range(n), repeat=2):
            counts[r + 1][c + 1][grid[r][c]] = 1
        for r, c, i in product(range(1, n + 1), range(1, n + 1), range(1, 11)):
            counts[r][c][i] += counts[r][c - 1][i]
        for r, c, i in product(range(1, n + 1), range(1, n + 1), range(1, 11)):
            counts[r][c][i] += counts[r - 1][c][i]
        q = int(input())
        for _ in range(q):
            x1, y1, x2, y2 = (int(input()) for _ in range(4))
            frequencies = [a - b - c + d for a, b, c, d in
                           zip(counts[x2][y2], counts[x1 - 1][y2], counts[x2][y1 - 1], counts[x1 - 1][y1 - 1])]
            answer = sum(i != 0 for i in frequencies)
            answers.append(f"{answer}")
print(*answers, sep="\n")
