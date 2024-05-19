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
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n, b = int(input()), int(input())
        x_sum = 0
        y_sum = 0
        for _ in range(n):
            x, y = int(input()), int(input())
            x_sum += x
            y_sum += y
        if x_sum == 0:
            answer = "EZPZ"
        else:
            denom, numer = x_sum, -n*b+y_sum
            denom, numer = denom // gcd(denom, numer), numer // gcd(denom, numer)
            if denom < 0:
                denom *= -1
                numer *= -1
            answer = f"{numer}/{denom}" if denom != 1 else f"{numer}"
        answers.append(f"{answer}")
    print(answers)