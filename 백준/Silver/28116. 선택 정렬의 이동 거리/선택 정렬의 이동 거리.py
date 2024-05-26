from bisect import bisect_left
from string import ascii_uppercase, ascii_lowercase
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
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        a = [0] + [int(input()) for _ in range(n)]
        positions = {v: i for i, v in enumerate(a)}
        dist = [0 for _ in range(n + 1)]
        for i, v in enumerate(a):
            if i == 0:
                continue
            if i != v:
                i_pos = positions[i]
                a[i], a[i_pos] = a[i_pos], a[i]
                dist[a[i]] += abs(i_pos - i)
                dist[a[i_pos]] += abs(i_pos - i)
                positions[a[i]], positions[a[i_pos]] = i, i_pos
        answer = " ".join(map(str, dist[1:]))
        answers.append(f"{answer}")
    print(answers)