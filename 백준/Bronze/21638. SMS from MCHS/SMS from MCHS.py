from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        t1, v1, t2, v2 = [int(input()) for _ in range(4)]
        answer = "No message"
        if t2 < 0 and v2 >= 10:
            answer = "A storm warning for tomorrow! Be careful and stay home if possible!"
        elif t2 < t1:
            answer = "MCHS warns! Low temperature is expected tomorrow."
        elif v2 > v1:
            answer = "MCHS warns! Strong wind is expected tomorrow."
        answers[h] = f"{answer}"
    print(answers)