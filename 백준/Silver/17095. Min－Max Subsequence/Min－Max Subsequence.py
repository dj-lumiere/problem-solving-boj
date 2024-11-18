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
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        A = [int(input()) for _ in range(N)]
        global_max = max(A)
        global_min = min(A)
        if global_max == global_min:
            answer = "1"
        else:
            last_max = last_min = -1
            min_length = INF
            for idx, num in enumerate(A):
                if num == global_max:
                    last_max = idx
                    if last_min != -1:
                        min_length = min(min_length, last_max - last_min + 1)
                if num == global_min:
                    last_min = idx
                    if last_max != -1:
                        min_length = min(min_length, last_min - last_max + 1)
            answer = str(min_length) if min_length != INF else "1"
        answers.append(f"{answer}")
    print(*answers)
