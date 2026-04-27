from bisect import bisect_left
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
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 998244353
    for hh in range(t):
        answer = []
        n = int(input())
        scores = [(int(input()), int(input())) for _ in range(n)]
        min_rss = 102938109281289123
        min_a = -1
        min_b = -1
        for a, b in product(range(1, 101), repeat=2):
            rss = sum((y - (a * x + b)) ** 2 for x, y in scores)
            if rss < min_rss:
                min_rss = rss
                min_a = a
                min_b = b
        eprint(min_rss)
        answers[hh] = f"{min_a} {min_b}"
    print(answers)