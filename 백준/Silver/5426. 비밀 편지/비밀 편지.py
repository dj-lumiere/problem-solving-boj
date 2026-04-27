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
    t = int(input())
    for hh in range(t):
        n = input().decode()
        grid = [["" for _ in range(int(len(n) ** .5))] for _ in range(int(len(n) ** .5))]
        for i, v in enumerate(n):
            x, y = divmod(i, int(len(n) ** .5))
            x, y = x, int(len(n) ** .5) - 1 - y
            grid[y][x] = v
        answer = "".join("".join(x) for x in grid)
        answers.append(f"{answer}")
    print(answers)