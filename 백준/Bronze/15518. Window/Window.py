from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n, h, w = int(input()), int(input()), int(input())
        xs = [int(input()) for _ in range(n)]
        intervals = []
        for i in range(1, n + 1):
            shift = xs[i - 1]
            start = w * (i - 1) + shift if i % 2 == 1 else w * (i - 1) - shift
            end = w * i + shift if i % 2 == 1 else w * i - shift
            if start > end:
                start, end = end, start
            intervals.append((start, end))
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(list(interval))
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        covered = sum(max(0, end - start) for start, end in merged)
        total = n * w
        open_area = (total - covered) * h
        answer = f"{open_area}"
        answers.append(f"{answer}")
    print(*answers)
