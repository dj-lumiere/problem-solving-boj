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
    for hh in range(t):
        my_dots = [[float(input()) for _ in range(2)] for _ in range(3)]
        opponent_dots = [[float(input()) for _ in range(2)] for _ in range(3)]
        n = 0
        m = 0
        for x, y in my_dots:
            d = sqrt(x * x + y * y)
            if d <= 3:
                n += 100
            elif d <= 6:
                n += 80
            elif d <= 9:
                n += 60
            elif d <= 12:
                n += 40
            elif d <= 15:
                n += 20
        for x, y in opponent_dots:
            d = sqrt(x * x + y * y)
            if d <= 3:
                m += 100
            elif d <= 6:
                m += 80
            elif d <= 9:
                m += 60
            elif d <= 12:
                m += 40
            elif d <= 15:
                m += 20
        if n == m:
            answer = f"SCORE: {n} to {m}, TIE."
        elif n > m:
            answer = f"SCORE: {n} to {m}, PLAYER 1 WINS."
        else:
            answer = f"SCORE: {n} to {m}, PLAYER 2 WINS."
        answers.append(f"{answer}")
    print(*answers, sep="\n")