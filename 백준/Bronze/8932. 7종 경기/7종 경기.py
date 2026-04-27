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
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    score = [lambda x: int(9.23076 * (26.7 - x) ** 1.835), lambda x: int(1.84523 * (x - 75) ** 1.348),
             lambda x: int(56.0211 * (x - 1.5) ** 1.05), lambda x: int(4.99087 * (42.5 - x) ** 1.81),
             lambda x: int(0.188807 * (x - 210) ** 1.41), lambda x: int(15.9803 * (x - 3.8) ** 1.04),
             lambda x: int(0.11193 * (254 - x) ** 1.88)]
    for hh in range(t):
        p = [int(input()) for _ in range(7)]
        answer = sum(score[i](v) for i, v in enumerate(p))
        answers.append(f"{answer}")
    print(*answers, sep="\n")