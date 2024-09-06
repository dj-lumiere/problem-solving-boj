from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
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
        mama_papa = [[0, 0]] + [[int(input()), int(input())] for _ in range(n)]
        mama_papa_alive = [[True, True] for _ in range(n + 1)]
        self_alive = [False] + [True for _ in range(n)]
        for i, (v1, v2) in enumerate(mama_papa):
            if v1 == 0:
                mama_papa_alive[i][0] = False
            if v2 == 0:
                mama_papa_alive[i][1] = False
        m = int(input())
        lost = [int(input()) for _ in range(m)]
        for v in lost:
            self_alive[v] = False
        for i, (v1, v2) in enumerate(mama_papa):
            if v1 in lost:
                mama_papa_alive[i][0] = False
            if v2 in lost:
                mama_papa_alive[i][1] = False
        answer = sum(all([v1, v2, v3]) for v1, (v2, v3) in zip(self_alive, mama_papa_alive))
        answers.append(f"{answer}")
print(*answers, sep="\n")
