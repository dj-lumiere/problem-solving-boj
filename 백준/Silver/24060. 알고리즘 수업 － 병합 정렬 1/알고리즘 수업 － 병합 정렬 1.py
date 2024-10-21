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
    MERGE = 1
    SORT = 2
    for hh in range(1, t + 1):
        n, k = int(input()), int(input())
        a = [0] + [int(input()) for _ in range(n)]
        temp = [0 for _ in range(n + 1)]
        stack = [[SORT, (1, n)]]
        answer = 0
        while stack:
            mode, arguments = stack.pop()
            if k <= 0:
                break
            if mode == SORT:
                p, r = arguments
                if p < r:
                    q = (p + r) // 2
                    stack.append([MERGE, (p, q, r)])
                    stack.append([SORT, (q + 1, r)])
                    stack.append([SORT, (p, q)])
            elif mode == MERGE:
                p, q, r = arguments
                i, j, t = p, q + 1, 1
                while i <= q and j <= r:
                    if a[i] <= a[j]:
                        temp[t] = a[i]
                        t += 1
                        i += 1
                    else:
                        temp[t] = a[j]
                        t += 1
                        j += 1
                while i <= q:
                    temp[t] = a[i]
                    t += 1
                    i += 1
                while j <= r:
                    temp[t] = a[j]
                    t += 1
                    j += 1
                i, t = p, 1
                while i <= r and k > 0:
                    a[i] = temp[t]
                    k -= 1
                    if k == 0:
                        answer = a[i]
                    i += 1
                    t += 1
        if k > 0:
            answer = -1
        answers.append(answer)
    print(*answers, sep="\n")
