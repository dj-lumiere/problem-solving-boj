from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
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


    def input():
        try:
            return next(tokens)
        except StopIteration:
            return None


    def print(*args, sep="\n", end=""):
        write(1, (sep.join(map(str, args)) + end).encode())


    def eprint(*args, sep="\n", end=""):
        write(2, (sep.join(map(str, args)) + end).encode())


    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    DELTA = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    DELTA2 = [(0, 1), (0, -1), (1, 0), (1, -1)]
    for hh in range(t):
        a, x, b, y, m = (int(input()) for _ in range(5))
        case_a = a + max((m - 30)*21, 0) * x
        case_b = b + max((m - 45)*21, 0) * y
        answer = f"{case_a} {case_b}"
        answers.append(f"{answer}")
    print(*answers)