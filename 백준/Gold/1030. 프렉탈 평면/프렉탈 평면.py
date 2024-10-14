import re
from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from datetime import datetime, time, timedelta
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from heapq import heapify, heappush, heappop
from inspect import stack
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from math import cos, comb, log, gcd, floor, log2, log10, log1p, pi, ceil, factorial, sin, sqrt, atan2, tau
from os import write
from random import randint, shuffle
from string import ascii_uppercase, ascii_lowercase
from sys import setrecursionlimit, stdout, stderr
from time import perf_counter_ns, sleep

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        s, n, k, r1, r2, c1, c2 = (int(input()) for _ in range(7))
        grid = [["0" for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
        digit_range = range(n)[(n - k) // 2:-(n - k) // 2]
        for r, c in product(range(r1, r2 + 1), range(c1, c2 + 1)):
            row_digits = [r // (n ** i) % n for i in range(s)]
            col_digits = [c // (n ** i) % n for i in range(s)]
            if any(i in digit_range and j in digit_range for i, j in zip(row_digits, col_digits)):
                grid[r - r1][c - c1] = "1"
        answers.append("\n".join("".join(v) for v in grid))
    print(*answers, sep="\n")
