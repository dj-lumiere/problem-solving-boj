from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from inspect import stack
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

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
    t = int(input())
    answers = []


    def find_set(grid, n, m):
        for i in range(n):
            for j in range(m - 2):
                if grid[i][j] == grid[i][j + 1] == grid[i][j + 2]:
                    return [(i + 1, j + 1), (i + 1, j + 2), (i + 1, j + 3)]
        for i in range(n - 2):
            for j in range(m):
                if grid[i][j] == grid[i + 1][j] == grid[i + 2][j]:
                    return [(i + 1, j + 1), (i + 2, j + 1), (i + 3, j + 1)]
        return None


    for hh in range(1, t + 1):
        n, m = int(input()), int(input())
        grid = [[input() for _ in range(m)] for _ in range(n)]
        result = find_set(grid, n, m)
        if result:
            answers.append(f"{result[0][0]} {result[0][1]} {result[1][0]} {result[1][1]} {result[2][0]} {result[2][1]}")
        else:
            answers.append("no set found")
    print(*answers, sep="\n")