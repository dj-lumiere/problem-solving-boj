import re
from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from datetime import datetime, time, timedelta
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from heapq import heapify, heappush, heappop
from inspect import stack
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from math import cos, comb, log, gcd, floor, log2, log10, log1p, pi, ceil, factorial, sin, sqrt, atan2, tau
from os import write
from random import randint, shuffle
from string import ascii_uppercase, ascii_lowercase
from sys import setrecursionlimit, stdout, stderr
from time import perf_counter_ns, sleep

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        s = input()
        dp = [[0 for _ in range(5)] for _ in range(n)]
        for i, v in enumerate(s):
            dp[i] = dp[i - 1][:]
            if v == "W":
                dp[i][0] += 1
                dp[i][0] %= MOD
            elif v == "H":
                dp[i][1] += dp[i - 1][0]
                dp[i][1] %= MOD
            elif v == "E":
                dp[i][2] += dp[i - 1][1]
                dp[i][2] %= MOD
                dp[i][3] += dp[i - 1][2]
                dp[i][3] %= MOD
                dp[i][4] += dp[i - 1][3] + dp[i - 1][4]
                dp[i][4] %= MOD
        eprint(*dp, sep="\n")
        answer = (dp[-1][3] + dp[-1][4]) % MOD
        answers.append(answer)
    print(*answers, sep="\n")
