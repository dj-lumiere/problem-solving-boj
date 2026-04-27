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
        n, k, s = [int(input()) for _ in range(3)]
        data = [int(input()) for _ in range(s)]
        histogram = [0 for _ in range(n)]
        for v in data:
            histogram[(v - 1) // k] += 1
        height = max(histogram)
        grid = [["." for _ in range(n)] for _ in range(height)] + [["-" for _ in range(n)]]
        for i, v in enumerate(histogram):
            for j in range(height - v, height):
                grid[j][i] = "#"
        answer = "\n".join("".join(x) for x in grid)
        answers.append(f"{answer}")
    print(answers)