from bisect import bisect_left
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
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    beat = [*range(1, 16)] + [*range(14, 1, -1)]
    for hh in range(t):
        x1, y1, x2, y2, x3, y3 = [int(input()) for _ in range(6)]
        a = (x2 - x1) ** 2 + (y2 - y1) ** 2
        b = (x3 - x2) ** 2 + (y3 - y2) ** 2
        c = (x1 - x3) ** 2 + (y1 - y3) ** 2
        if a + b == c:
            x4, y4 = (x1 + x3) - x2, (y1 + y3) - y2
        elif a + c == b:
            x4, y4 = (x2 + x3) - x1, (y2 + y3) - y1
        elif b + c == a:
            x4, y4 = (x1 + x2) - x3, (y1 + y2) - y3
        else:
            x4, y4 = 0, 0
        answer = f"{x4} {y4}"
        answers.append(f"{answer}")
    print(answers)