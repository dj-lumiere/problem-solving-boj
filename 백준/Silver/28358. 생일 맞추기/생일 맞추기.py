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
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    result = [0 for _ in range(1024)]
    for mask in range(1 << 10):
        for i in range(1, 13):
            for j in range(1, [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][i] + 1):
                if not any(str(k) in str(i) + str(j) and mask & (1 << k) != 0 for k in range(10)):
                    result[mask] += 1
    for h in range(t):
        numbers = sum([int(input()) << i for i in range(10)])
        answers[h] = f"{result[numbers]}"
    print(answers)