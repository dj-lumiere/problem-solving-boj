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
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        colors = [[int(input()) for _ in range(3)] for _ in range(n)]
        distance = 0
        index = []
        for (i1, (r1, g1, b1)), (i2, (r2, g2, b2)) in combinations(enumerate(colors, start=1), r=2):
            if (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2 > distance:
                distance = (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
                index = [[i1, i2]]
            elif (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2 == distance:
                index.append([i1, i2])
        index.sort(key=lambda x: (x[0], x[1]))
        answers[h] = f"Data Set {h + 1}:\n" + "\n".join(" ".join(map(str, x)) for x in index)
    print(answers)