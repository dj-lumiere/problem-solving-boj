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
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        r = int(input())
        c = int(input())
        grid = [[int(input()) for _ in range(c)] for _ in range(r)]
        answer1 = 0
        answer2 = 0
        for i in range(r - 1):
            for j in range(c):
                if grid[i][j] == 1 and grid[i + 1][j] == 1:
                    answer1 += 1
        for i in range(r):
            for j in range(c - 1):
                if grid[i][j] == 1 and grid[i][j + 1] == 1:
                    answer1 += 1
        for i in range(r - 1):
            for j in range(c - 1):
                if grid[i][j] == 1 and grid[i + 1][j + 1] == 1:
                    answer2 += 1
        for i in range(1, r):
            for j in range(c - 1):
                if grid[i][j] == 1 and grid[i - 1][j + 1] == 1:
                    answer2 += 1
        answers[h] = f"{answer1} {answer1 + answer2}"
    print(answers)