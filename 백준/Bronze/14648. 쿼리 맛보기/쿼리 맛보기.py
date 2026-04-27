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
    n = int(input())
    t = int(input())
    x = [0] + [int(input()) for _ in range(n)]
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for hh in range(t):
        q = int(input())
        answer = 0
        if q == 1:
            a, b = int(input()), int(input())
            answer = sum(x[a:b + 1])
            x[a], x[b] = x[b], x[a]
        elif q == 2:
            a, b, c, d = [int(input()) for _ in range(4)]
            answer = sum(x[a:b + 1]) - sum(x[c:d + 1])
        answers[hh] = f"{answer}"
    print(answers)