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
        a = [int(input()) for _ in range(n)]
        inversion_count1 = 0
        inversion_count2 = 1
        for (i, v1), (j, v2) in product(enumerate(a), enumerate(a)):
            if i == j:
                continue
            if i < j and v1 > v2:
                inversion_count1 += 1
        a.reverse()
        for (i, v1), (j, v2) in product(enumerate(a), enumerate(a)):
            if i == j:
                continue
            if i < j and v1 > v2:
                inversion_count2 += 1
        answer = min(inversion_count1, inversion_count2)
        answers.append(f"{answer}")
    print(answers)