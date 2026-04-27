from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
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

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    target = [tuple(int(input()) for _ in range(3)) for _ in range(16)]
    for hh in range(t):
        a, b, c = int(input()), int(input()), int(input())
        if a == -1 and b == -1 and c == -1:
            break
        min_dist = INF
        nearest = None
        for tc in target:
            dist = (a - tc[0]) ** 2 + (b - tc[1]) ** 2 + (c - tc[2]) ** 2
            if dist < min_dist:
                min_dist = dist
                nearest = tc
        answer = f"({a},{b},{c}) maps to ({nearest[0]},{nearest[1]},{nearest[2]})"
        answers.append(f"{answer}")
    print(*answers)
