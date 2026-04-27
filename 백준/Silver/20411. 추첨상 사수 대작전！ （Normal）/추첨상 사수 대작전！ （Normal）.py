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
    for hh in range(t):
        m, seed, x1, x2 = [int(input()) for _ in range(4)]
        answer = ""
        # (a*seed+c)%m=x1, (a*x1+c)%m=x2
        for c in range(m):
            a1 = ((x1 - c) * pow(seed, -1, m)) % m
            a2 = ((x2 - c) * pow(x1, -1, m)) % m
            if a1 == a2:
                answer = f"{a1} {c}"
                break
        answers[hh] = f"{answer}"
    print(answers)