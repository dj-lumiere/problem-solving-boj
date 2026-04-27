from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
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

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 0
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        pass
    while True:
        t += 1
        o, w = int(input()), int(input())
        if o == w == 0:
            break
        while True:
            op, n = input().decode(), int(input())
            if op == "#":
                break
            if w != 0 and op == "E":
                w -= n
            if w != 0 and op == "F":
                w += n
            if w <= 0:
                w = 0
                continue
        state = "RIP"
        if o // 2 < w < o * 2:
            state = ":-)"
        elif w != 0:
            state = ":-("
        answer = f"{t} {state}"
        answers.append(f"{answer}")
    print(answers)