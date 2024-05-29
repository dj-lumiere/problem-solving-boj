from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
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
    beat = [*range(1, 16)] + [*range(14, 1, -1)]
    for hh in range(t):
        n = int(input())
        fib = [0, 1, 1]
        fib_sum = [0, 1, 2]
        for _ in range(100):
            fib.append(sum(fib[-2:]))
            fib_sum.append(fib_sum[-1] + fib[-1])
        answer = bisect_left(fib_sum, n)
        answers.append(f"{answer}")
    print(answers)