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
    t = 1
    for hh in range(t):
        winner = "DRAW"
        a1, b1 = map(int, input().split(b":"))
        b2, a2 = map(int, input().split(b":"))
        for i, j in product(range(20), repeat=2):
            a3, b3 = a2 + i, b2 + j
            if a1 + a3 > b1 + b3:
                winner = "A"
            elif a1 + a3 < b1 + b3:
                winner = "B"
            elif b1 > a3:
                winner = "B"
            elif b1 < a3:
                winner = "A"
            else:
                winner = "DRAW"
            if winner == "DRAW":
                eprint(i, j)
                break
        answer = "YES" if winner == "DRAW" else "NO"
        answers.append(f"{answer}")
    print(answers)