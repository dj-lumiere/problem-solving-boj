from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        k, p, q, r, s, a1 = (int(input()) for _ in range(6))
        sum_dict = {1: a1}


        def s_n(n):
            if n in sum_dict:
                return sum_dict[n]
            if n % 2 == 1:
                sub1, sub2 = n // 2, n // 2
            else:
                sub1, sub2 = n // 2, n // 2 - 1
            sub_result1 = sum_dict[sub1] if sub1 in sum_dict else s_n(sub1)
            sub_result2 = sum_dict[sub2] if sub2 in sum_dict else s_n(sub2)
            sum_dict[n] = (a1 + p * sub_result1 + q * sub1 + r * sub_result2 + s * sub2) % MOD
            return sum_dict[n]


        answer = s_n(2 ** k - 1)
        answers.append(f"{answer}")
    print(*answers, sep="\n")