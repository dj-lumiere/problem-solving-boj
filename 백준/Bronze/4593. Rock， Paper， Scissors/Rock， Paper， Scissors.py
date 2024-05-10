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
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        pass
    while True:
        p1 = input().decode()
        p2 = input().decode()
        if p1 == p2 == "E":
            break
        p1_win = 0
        p2_win = 0
        for i, j in zip(p1, p2):
            if (i == "R" and j == "S") or (i == "P" and j == "R") or (i == "S" and j == "P"):
                p1_win += 1
            if (j == "R" and i == "S") or (j == "P" and i == "R") or (j == "S" and i == "P"):
                p2_win += 1
        answers.append(f"P1: {p1_win}\nP2: {p2_win}")
    print(answers)