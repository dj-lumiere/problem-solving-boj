from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import stdout, stderr, setrecursionlimit
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, pairwise, permutations, combinations_with_replacement, product, zip_longest, chain
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
    losing_hand = {"R": "P", "P": "S", "S": "R"}
    for hh in range(t):
        dots = [(int(input()), int(input())) for _ in range(3)]
        dots.append(dots[0])
        r = float(input())
        a, b, c = [((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5 for (x1, y1), (x2, y2) in pairwise(dots)]
        area = (4 * a * a * b * b - (a * a + b * b - c * c) ** 2) ** .5 / 4
        r2 = area * 2 / (a + b + c)
        answer = (r2 - r) / r * 100
        answers.append(f"{answer}")
    print(*answers, sep="\n")