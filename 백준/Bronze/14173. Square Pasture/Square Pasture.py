from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

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
        points = [int(input()) for _ in range(8)]
        x = max(v for i, v in enumerate(points) if i & 1 == 0) - min(v for i, v in enumerate(points) if i & 1 == 0)
        y = max(v for i, v in enumerate(points) if i & 1 == 1) - min(v for i, v in enumerate(points) if i & 1 == 1)
        answer = max(x, y) ** 2
        answers[h] = f"{answer}"
    print(answers)