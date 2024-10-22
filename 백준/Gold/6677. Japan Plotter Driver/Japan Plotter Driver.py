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
    t = INF
    answers = []
    for hh in range(1, t + 1):
        x, y = int(input()), int(input())
        if x == y == 0:
            break
        answer = INF
        grid = [[[] for _ in range(x + 2)] for _ in range(y + 2)]
        for i in range(x + 2):
            grid[0][i].append("-")
            grid[-1][i].append("-")
        for i in range(y + 2):
            grid[i][0].append("|")
            grid[i][-1].append("|")
        while command := input():
            if command == "PRINT":
                print_grid = [[" " for _ in range(x + 2)] for _ in range(y + 2)]
                for r, c in product(range(y + 2), range(x + 2)):
                    if not grid[r][c]:
                        continue
                    unique_letter_added = set(grid[r][c])
                    if len(unique_letter_added) == 1:
                        print_grid[r][c] = list(unique_letter_added)[0]
                    elif unique_letter_added == set("|-"):
                        print_grid[r][c] = "+"
                    elif unique_letter_added == set(r"\/"):
                        print_grid[r][c] = "x"
                    else:
                        print_grid[r][c] = "*"
                answer = "\n".join("".join(v) for v in print_grid)
                break
            if command == "POINT":
                x1, y1 = int(input()), int(input())
                grid[y1][x1].append("o")
            if command == "TEXT":
                x1, y1, txt = int(input()), int(input()), input()
                for i, v in enumerate(txt, start=x1):
                    if not is_inbound(i - 1, x, y1 - 1, y):
                        break
                    grid[y1][i].append(v)
            if command == "LINE":
                x1, y1, x2, y2 = (int(input()) for _ in range(4))
                if x1 == x2:
                    y1, y2 = min(y1, y2), max(y1, y2)
                    for i in range(y1, y2 + 1):
                        if not is_inbound(x1 - 1, x, i - 1, y):
                            continue
                        grid[i][x1].append("|")
                elif y1 == y2:
                    x1, x2 = min(x1, x2), max(x1, x2)
                    for i in range(x1, x2 + 1):
                        if not is_inbound(i - 1, x, y1 - 1, y):
                            continue
                        grid[y1][i].append("-")
                elif (x2 - x1) * (y2 - y1) < 0:  # slope is positive
                    x1, x2 = min(x1, x2), max(x1, x2)
                    y1, y2 = min(y1, y2), max(y1, y2)
                    for i, j in zip(range(x1, x2 + 1), reversed(range(y1, y2 + 1))):
                        if not is_inbound(i - 1, x, j - 1, y):
                            continue
                        grid[j][i].append("/")
                else:  # slope is negative
                    x1, x2 = min(x1, x2), max(x1, x2)
                    y1, y2 = min(y1, y2), max(y1, y2)
                    for i, j in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                        if not is_inbound(i - 1, x, j - 1, y):
                            continue
                        grid[j][i].append("\\")
            if command == "CLEAR":
                x1, y1, x2, y2 = (int(input()) for _ in range(4))
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = min(y1, y2), max(y1, y2)
                for r, c in product(range(y1, y2 + 1), range(x1, x2 + 1)):
                    if not is_inbound(c - 1, x, r - 1, y):
                        continue
                    grid[r][c].clear()
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")
