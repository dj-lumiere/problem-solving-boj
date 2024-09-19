from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, m, k = int(input()), int(input()), int(input())
        # 0, 1, ..., n을 m번 사용해 가지고 k를 만들기
        dp = [[0 for _ in range(n * m + n + 2)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(n + 1):
            dp[1][i] = i + 1
        for i in range(n + 1, n * m + 1):
            dp[1][i] = n + 1
        for i, j in product(range(2, m + 1), range(n * m + 1)):
            dp[i & 1][j] = dp[i & 1][j - 1] + (dp[(i - 1) & 1][j] - dp[(i - 1) & 1][j - n - 1]) % MOD
        answer = (dp[m & 1][k] - dp[m & 1][k - 1]) % MOD
        answers.append(f"{answer}")
print(*answers, sep="\n")
