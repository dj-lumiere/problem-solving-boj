from bisect import bisect_left, bisect_right
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
    MOD = 1_000_000_007
    for hh in range(t):
        is_related = False
        is_friendly = False
        is_tied = False
        answer = 0
        n = Counter(map(int, input().decode()))
        if not any(i in n for i in [i for i in range(10) if not i in [2, 0, 1, 8]]):
            is_related = True
            if all(i in n for i in [2, 0, 1, 8]):
                is_friendly = True
                if all(n[i] == n[2] for i in [2, 0, 1, 8]):
                    is_tied = True
        if is_related and not is_friendly:
            answer = 1
        elif is_friendly and not is_tied:
            answer = 2
        elif is_tied:
            answer = 8
        answers.append(f"{answer}")
    print(answers)