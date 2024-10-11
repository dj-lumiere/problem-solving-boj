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
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        DELTA = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        N = int(input())
        last_visited = {}
        x, y = 0, 0
        time = 0
        min_time_diff = INF
        revisited = False
        last_visited[(x, y)] = time
        for _ in range(N):
            direction = input()
            steps = int(input())
            dx, dy = DELTA[direction]
            for _ in range(steps):
                x += dx
                y += dy
                time += 1
                if (x, y) in last_visited:
                    revisited = True
                    min_time_diff = min(min_time_diff, time - last_visited[(x, y)])
                last_visited[(x, y)] = time
        if revisited:
            answers.append(min_time_diff)
        else:
            answers.append(-1)
    print(*answers, sep="\n")
