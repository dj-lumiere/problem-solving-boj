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
        n = int(input())
        x = []
        y = []
        gradient = []
        for _ in range(n):
            x2, y2 = int(input()), int(input())
            x.append(x2)
            y.append(y2)
        for (i1, j1), (i2, j2) in zip(zip(x, y), zip(x[1:], y[1:])):
            if j1 < j2:
                gradient.append(1)
            elif j1 == j2:
                gradient.append(0)
            else:
                gradient.append(-1)
        m = int(input())
        answer2 = []
        for _ in range(m):
            k = float(input())
            answer2.append(gradient[bisect_left(x, k)-1])
        answer = "\n".join(map(str, answer2))
        answers.append(f"{answer}")
    print(answers)