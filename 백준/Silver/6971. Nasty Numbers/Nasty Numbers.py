from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        pairs = []
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                pairs.append((i, n // i))
        is_nasty = False
        for (i1, j1), (i2, j2) in permutations(pairs, 2):
            if abs(i1 - j1) == i2 + j2:
                is_nasty = True
                break
        answer = f"{n} is {'' if is_nasty else 'not '}nasty"
        answers[h] = f"{answer}"
    print(answers)