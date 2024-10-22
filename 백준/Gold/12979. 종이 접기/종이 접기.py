import re
from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from datetime import datetime, time, timedelta
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from math import cos, comb, log, gcd, floor, log2, log10, log1p, pi, ceil, factorial, sin, sqrt, atan2, tau
from os import write
from random import randint, shuffle
from string import ascii_uppercase, ascii_lowercase
from sys import setrecursionlimit, stdout, stderr
from time import perf_counter_ns, sleep

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        w, h, a = (int(input()) for _ in range(3))
        possible_pairs = []
        fold_count = INF
        for i in range(1, int(a ** .5) + 1):
            if a % i:
                continue
            possible_pairs.extend([(i, a // i), (a // i, i)])
        for x, y in possible_pairs:
            if w < x or h < y:
                continue
            x_fold_count = ((w + x - 1) // x - 1).bit_length()
            y_fold_count = ((h + y - 1) // y - 1).bit_length()
            fold_count = min(fold_count, x_fold_count + y_fold_count)
        answer = -1 if fold_count == INF else fold_count
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")
