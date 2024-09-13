from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        nodes = [(int(input()), int(input())) for _ in range(n - 1)]
        degrees = [0 for _ in range(n + 1)]
        d_tree = 0
        g_tree = 0
        for i, j in nodes:
            degrees[i] += 1
            degrees[j] += 1
        for i, j in nodes:
            if degrees[i] >= 2 and degrees[j] >= 2:
                d_tree += comb(degrees[i] - 1, 1) * comb(degrees[j] - 1, 1)
        for v in degrees:
            if v >= 3:
                g_tree += comb(v, 3)
        answer = "DUDUDUNGA"
        if d_tree > g_tree * 3:
            answer = "D"
        elif d_tree < g_tree * 3:
            answer = "G"
        answers.append(f"{answer}")
print(*answers, sep="\n")
