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
        p = int(input())
        q = int(input())
        a = [int(input()) for _ in range(n)]
        b = [int(input()) for _ in range(n)]
        count = [0 for _ in range(n)]
        is_possible = True
        for i, (a1, b1) in enumerate(zip(a, b)):
            count_sub, remainder = divmod((a1 - b1), (p - q)) if p != q else (0, a1 - b1)
            if count_sub > 0 or remainder != 0:
                is_possible = False
                break
            count[i] = -count_sub
        answer = "YES\n" + " ".join(map(str, count)) if is_possible else "NO"
        answers.append(f"{answer}")
    print(answers)