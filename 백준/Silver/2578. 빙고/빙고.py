from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop, heapify
from itertools import combinations, pairwise, permutations, combinations_with_replacement, product, zip_longest, chain, groupby
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
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 998244353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        numbers = [int(input()) for _ in range(25)]
        check = [False for _ in range(25)]
        bingos = ([[i * 5 + j for j in range(5)] for i in range(5)]
                  + [[j * 5 + i for j in range(5)] for i in range(5)]
                  + [[4 + 4 * i for i in range(5)]]
                  + [[6 * i for i in range(5)]])
        calls = [int(input()) for _ in range(25)]
        answer = 0
        for i, v in enumerate(calls, start=1):
            check[numbers.index(v)] = True
            if sum(all(check[i] for i in j) for j in bingos) >= 3:
                answer = i
                break
        answers.append(f"{answer}")
print(*answers, sep="\n")