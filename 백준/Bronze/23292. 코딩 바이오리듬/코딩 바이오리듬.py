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
    INF = 10 ** 18
    for hh in range(t):
        start = input().decode()
        n = int(input())
        days = [input().decode() for _ in range(n)]
        biorhythms = []
        days.sort()
        for v in days:
            biorhythm = [0, 0, 0]
            for i, (v2, v3) in enumerate(zip(map(int, start), map(int, v))):
                if i < 4:
                    biorhythm[0] += (v2 - v3) ** 2
                elif i < 6:
                    biorhythm[1] += (v2 - v3) ** 2
                else:
                    biorhythm[2] += (v2 - v3) ** 2
            biorhythms.append(reduce(lambda x, y: x * y, biorhythm))
        answer = days[biorhythms.index(max(biorhythms))]
        answers.append(f"{answer}")
    print(answers)