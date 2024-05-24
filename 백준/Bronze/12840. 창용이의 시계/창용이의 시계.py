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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        h, m, s = int(input()), int(input()), int(input())
        result = []
        current_time = h * 3600 + m * 60 + s
        q = int(input())
        for _ in range(q):
            T = int(input())
            if T == 1:
                d = int(input())
                current_time += d
                current_time %= 86400
            if T == 2:
                d = int(input())
                current_time -= d
                current_time %= 86400
            if T == 3:
                result.append(f"{current_time // 3600 % 24} {current_time // 60 % 60} {current_time % 60}")
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(answers)