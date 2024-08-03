from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
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
    input = lambda: next(tokens) if tokens else ""
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        k = int(input())
        a = [0] + [int(input()) for _ in range(n)]
        finished = False
        answer = 0
        for i in range(2, n + 1):
            loc = i - 1
            newItem = a[i]
            while 1 <= loc and newItem < a[loc] and not finished:
                a[loc + 1] = a[loc]
                k -= 1
                if k == 0:
                    finished = True
                loc -= 1
            if loc + 1 != i and not finished:
                a[loc + 1] = newItem
                k -= 1
                if k == 0:
                    finished = True
        answer = " ".join(map(str, a[1:])) if finished else "-1"
        answers.append(f"{answer}")
    print(*answers)