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
    MOD = 11092019
    for h in range(t):
        l = int(input())
        n = int(input())
        t = int(input())
        balls = [0, l]
        direction = [0, 0]
        for _ in range(n):
            s, c = int(input()), -1 if input().decode() == "L" else 1
            balls.append(s)
            direction.append(c)
        collision = 0
        for _ in range(t):
            for i in range(n + 2):
                balls[i] += direction[i]
            for i in range(n + 2):
                for j in range(n + 2):
                    if i < j and balls[i] == balls[j]:
                        direction[i] *= -1
                        direction[j] *= -1
                        if i not in (0, 1):
                            collision += 1
        answers[h] = f"{collision}"
    print(answers)