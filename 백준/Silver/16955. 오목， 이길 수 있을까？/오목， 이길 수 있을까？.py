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
        grid = [list(input().decode()) for _ in range(10)]
        answer = 0
        for r, c in product(range(10), range(6)):
            checks = Counter([grid[r][c + i] for i in range(5)])
            for letter in "XO.":
                if letter not in checks:
                    checks[letter] = 0
            if checks["X"] == 4 and checks["O"] == 0 and checks["."] == 1:
                answer = 1
        for r, c in product(range(6), range(10)):
            checks = Counter([grid[r + i][c] for i in range(5)])
            for letter in "XO.":
                if letter not in checks:
                    checks[letter] = 0
            if checks["X"] == 4 and checks["O"] == 0 and checks["."] == 1:
                answer = 1
        for r, c in product(range(6), range(6)):
            checks = Counter([grid[r + i][c + i] for i in range(5)])
            for letter in "XO.":
                if letter not in checks:
                    checks[letter] = 0
            if checks["X"] == 4 and checks["O"] == 0 and checks["."] == 1:
                answer = 1
        for r, c in product(range(4, 10), range(6)):
            checks = Counter([grid[r - i][c + i] for i in range(5)])
            for letter in "XO.":
                if letter not in checks:
                    checks[letter] = 0
            if checks["X"] == 4 and checks["O"] == 0 and checks["."] == 1:
                answer = 1
        answers.append(f"{answer}")
    print(answers)