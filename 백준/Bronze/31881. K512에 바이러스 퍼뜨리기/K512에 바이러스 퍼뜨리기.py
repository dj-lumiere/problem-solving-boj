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
        n = int(input())
        q = int(input())
        status = [False for _ in range(n + 1)]
        infection_count = 0
        result = []
        for _ in range(q):
            op = int(input())
            if op == 1:
                x = int(input())
                infection_count += 1 - status[x]
                status[x] = True
            if op == 2:
                x = int(input())
                infection_count -= status[x]
                status[x] = False
            if op == 3:
                result.append(n - infection_count)
        answer = "\n".join(map(str, result))
        answers.append(f"{answer}")
    print(answers)