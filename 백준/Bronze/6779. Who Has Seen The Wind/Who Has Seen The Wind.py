from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import stdout, stderr, setrecursionlimit
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, pairwise, permutations, combinations_with_replacement, product, zip_longest, chain
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from array import array
import re

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    losing_hand = {"R": "P", "P": "S", "S": "R"}
    for hh in range(t):
        h = int(input())
        m = int(input())
        A = lambda t: -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
        answer = "The balloon does not touch ground in the given time."
        for i in range(1, m + 1):
            if A(i) <= 0:
                answer = f"The balloon first touches ground at hour: {i}"
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")