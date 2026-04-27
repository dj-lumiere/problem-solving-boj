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
    MOD = 998244353
    for hh in range(t):
        pass
    while True:
        t += 1
        n = int(input())
        if n < 0:
            break
        m_sum = 0
        mx_sum = 0
        my_sum = 0
        for _ in range(n):
            x, y, m = [int(input()) for _ in range(3)]
            m_sum += m
            mx_sum += m * x
            my_sum += m * y
        answer = f"Case {t}: {mx_sum / m_sum:.2f} {my_sum / m_sum:.2f}"
        answers.append(answer)
    print(answers)