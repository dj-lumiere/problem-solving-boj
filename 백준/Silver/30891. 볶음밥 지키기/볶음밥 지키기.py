from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n, r = int(input()), int(input())
        rices = [(int(input()), int(input())) for _ in range(n)]
        max_rice = -1
        max_pos = (-200, -200)
        for x, y in product(range(-100 - r, 101 + r), repeat=2):
            keep_rice = sum((xi - x) ** 2 + (yi - y) ** 2 <= r ** 2 for xi, yi in rices)
            if keep_rice > max_rice:
                max_rice = keep_rice
                max_pos = (x, y)
        x, y = max_pos
        answer = f"{x} {y}"
        answers.append(f"{answer}")
    print(answers)