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
    for hh in range(t):
        n = int(input())
        m = int(input())
        grid = [[[False for _ in range(n + 2)] for _ in range(n + 2)] for _ in range(n + 2)]
        answer = 0
        for _ in range(m):
            i, j, k = int(input()), int(input()), int(input())
            grid[i][j][k] = True
        for i, j, k in product(range(1, n + 1), repeat=3):
            if all(grid[i + di][j + dj][k + dk] for di, dj, dk in
                   [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (0, 0, 0)]):
                answer += 1
        answers.append(f"{answer}")
    print(answers)