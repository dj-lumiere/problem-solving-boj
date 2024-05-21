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
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        available = [False for _ in range(77)]
        names = {}
        for _ in range(n):
            s, w, d, p = [input().decode()] + [int(input()) for _ in range(3)]
            names[s] = (w * 7 + d, p)
        for _ in range(n):
            s, m = input().decode(), int(input())
            if m >= names[s][1]:
                available[names[s][0]] = True
        max_available_combo = 0
        current_combo = 0
        for i, v in enumerate(available):
            if v:
                current_combo += 1
            else:
                max_available_combo = max(current_combo, max_available_combo)
                current_combo = 0
        max_available_combo = max(current_combo, max_available_combo)
        answer = max_available_combo
        answers.append(f"{answer}")
    print(answers)