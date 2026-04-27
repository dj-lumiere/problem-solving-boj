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
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    for hh in range(t):
        e = int(input())
        a = int(input())
        multiplier = [(-1, 1), (1, 5), (5, 25), (25, 125), (125, 625), (625, 3125), (3125, 15625), (15625, 78125),
                      (78125, 390625), (390625, 1953125)]
        drought_word = "drought"
        for i, (v1, v2) in enumerate(multiplier):
            if v1 * a < e <= v2 * a:
                if i == 0:
                    drought_word = "no drought"
                else:
                    drought_word = " ".join(["mega"] * (i - 1) + [drought_word])
                break
        answer = f"""Data Set {hh+1}:
{drought_word}
"""
        answers.append(f"{answer}")
    print(*answers, sep="\n")