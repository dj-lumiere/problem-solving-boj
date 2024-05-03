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
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        cows = [(int(input()), int(input())) for _ in range(n)]
        dist = 0
        answer = [0, 0]
        for (i1, (x1, y1)), (i2, (x2, y2)) in combinations(enumerate(cows, start=1), 2):
            dist_sub = (x2 - x1) ** 2 + (y2 - y1) ** 2
            if dist_sub > dist:
                dist = dist_sub
                answer = [i1, i2]
        answer.sort()
        answers[h] = f"{answer[0]} {answer[1]}"
    print(answers)