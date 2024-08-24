from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, pairwise, permutations, combinations_with_replacement, product, zip_longest, chain
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    dp = [[0, 0] for _ in range(45)]
    for i in range(1, 45):
        if i == 1:
            dp[i][0] = dp[i][1] = 1
            continue
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]
    for hh in range(t):
        n = int(input())
        answer = f"Scenario #{hh + 1}:\n{sum(dp[n])}\n"
        answers.append(f"{answer}")
print(*answers, sep="\n")