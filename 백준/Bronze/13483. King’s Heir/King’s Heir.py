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
        d0, m0, y0 = [int(input()) for _ in range(3)]
        n = int(input())
        sons = [tuple(int(input()) for _ in range(3)) for _ in range(n)]
        answer = 0
        for i, (d, m, y) in enumerate(sons, start=1):
            if y0 - y > 18 or (y0 - y == 18 and (m, d) <= (m0, d0)):
                if not answer:
                    answer = i
                elif sons[answer - 1][::-1] < (y, m, d):
                    answer = i
        if not answer:
            answer = -1
        answers[hh] = f"{answer}"
        print(answers)