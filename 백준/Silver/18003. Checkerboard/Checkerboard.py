from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
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
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        r, c, v, h = int(input()), int(input()), int(input()), int(input())
        grid = [[0 for _ in range(c)] for _ in range(r)]
        row_seperation = [0]
        col_seperation = [0]
        for i in range(v):
            row_seperation.append(row_seperation[-1] + int(input()))
        for i in range(h):
            col_seperation.append(col_seperation[-1] + int(input()))
        for i, (v1, v2) in enumerate(zip(row_seperation, row_seperation[1:])):
            for j in range(v1, v2):
                for k in range(c):
                    grid[j][k] += i
        for i, (h1, h2) in enumerate(zip(col_seperation, col_seperation[1:])):
            for j in range(r):
                for k in range(h1, h2):
                    grid[j][k] += i
        answer = "\n".join("".join("B" if grid[i][j] % 2 == 0 else "W" for j in range(c)) for i in range(r))
        answers.append(f"{answer}")
    print(answers)