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
    MOD = 1000000007
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        movement = [(0, 0)]
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(100):
            length = i // 2 + 1
            direction = delta[i % 4]
            dx, dy = direction
            for j in range(length):
                x, y = movement[-1]
                movement.append((x + dx, y + dy))
        x, y = movement[n]
        answer = f"{x} {y}"
        answers.append(f"{answer}")
    print(answers)