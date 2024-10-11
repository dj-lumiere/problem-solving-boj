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
        NR = int(input())
        NC = int(input())
        grid = []
        for i in range(NR):
            row = []
            for j in range(NC):
                row.append(int(input()))
            grid.append(row)
        max_sum = -1
        best_row = -1
        best_col = -1
        for i in range(NR - 2):
            for j in range(NC - 2):
                current_sum = 0
                for x in range(3):
                    for y in range(3):
                        current_sum += grid[i + x][j + y]
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_row = i + 1
                    best_col = j + 1
        answers.extend([max_sum, best_row, best_col])
    print(*answers, sep="\n")
