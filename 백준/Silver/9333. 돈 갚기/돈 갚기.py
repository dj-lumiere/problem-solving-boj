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
        (r1, r2), (b1, b2), (
        m1, m2) = map(int, input().split(b".")), map(int, input().split(b".")), map(int, input().split(b"."))
        r = r1 * 100 + r2
        b = b1 * 100 + b2
        m = m1 * 100 + m2
        answer = "impossible"
        for i in range(1, 1201):
            b, mod = divmod(b * (10000 + r), 10000)
            if mod >= 5000:
                b += 1
            b -= m
            if b <= 0:
                answer = i
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")