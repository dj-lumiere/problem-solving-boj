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
from inspect import stack
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
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        x, y, n = (int(input()) for _ in range(3))
        x += 500
        y += 500
        has_puddle = [[False for _ in range(1001)] for _ in range(1001)]
        for _ in range(n):
            a, b = (int(input()) + 500 for _ in range(2))
            has_puddle[b][a] = True
        distance = [[0 for _ in range(1001)] for _ in range(1001)]
        distance[500][500] = 1
        queue = deque([(500, 500)])
        while queue:
            current_x, current_y = queue.popleft()
            if current_x == x and current_y == y:
                break
            for dx, dy in DELTA:
                next_x, next_y = current_x + dx, current_y + dy
                if not is_inbound(next_x, 1001, next_y, 1001):
                    continue
                if has_puddle[next_y][next_x]:
                    continue
                if distance[next_y][next_x]:
                    continue
                distance[next_y][next_x] = distance[current_y][current_x] + 1
                queue.append((next_x, next_y))
        answer = distance[y][x] - 1
        answers.append(answer)
    print(*answers, sep="\n")
