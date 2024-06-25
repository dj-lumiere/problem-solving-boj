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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    for hh in range(t):
        n, m = int(input()), int(input())
        a = [int(input()) for _ in range(n)]
        b = sorted([-INF, -INF] + [int(input()) for _ in range(m)] + [INF, INF])
        c = [0] * n
        for i, v in enumerate(a):
            b_left = b[bisect_left(b, v) - 1]
            b_mid = b[bisect_left(b, v)]
            b_right = b[bisect_left(b, v) + 1]
            c_candidate = [b_left, b_mid, b_right]
            if abs(v - b_left) == min(map(lambda x: abs(x - v), c_candidate)):
                c[i] = b_left
            elif abs(v - b_mid) == min(map(lambda x: abs(x - v), c_candidate)):
                c[i] = b_mid
            else:
                c[i] = b_right
        answer = sum(c)
        answers.append(f"{answer}")
    print(answers)