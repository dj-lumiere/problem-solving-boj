from sys import stdin
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        x, y = int(input()), int(input())
        for _ in range(n-1):
            dir, d = input().decode(), int(input())
            if dir == "N":
                y += d
            elif dir == "NE":
                y += d / sqrt(2)
                x += d / sqrt(2)
            elif dir == "E":
                x += d
            elif dir == "SE":
                x += d / sqrt(2)
                y -= d / sqrt(2)
            elif dir == "S":
                y -= d
            elif dir == "SW":
                x -= d / sqrt(2)
                y -= d / sqrt(2)
            elif dir == "W":
                x -= d
            elif dir == "NW":
                x -= d / sqrt(2)
                y += d / sqrt(2)
        answer = f"{x} {y}"
        answers.append(f"{answer}")
    print(*answers)
