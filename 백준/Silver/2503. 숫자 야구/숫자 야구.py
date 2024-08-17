from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import stdout, stderr, setrecursionlimit
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from array import array
import re

getcontext().prec = 1000


def strikes(a, b):
    return sum(i == j for i, j in zip(str(a), str(b)))


def balls(a, b):
    digit_count_a = Counter(str(a))
    digit_count_b = Counter(str(b))
    intersection = 0
    for k, v in digit_count_a.items():
        if k in digit_count_b:
            intersection += min(v, digit_count_b[k])
    return intersection - strikes(a, b)


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
        cases = [(int(input()), int(input()), int(input())) for _ in range(n)]
        answer = 0
        for a in ("".join(map(str, x)) for x in permutations(range(1, 10), r=3)):
            if all(strikes(a, i) == j and balls(a, i) == k for i, j, k in cases):
                answer += 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")