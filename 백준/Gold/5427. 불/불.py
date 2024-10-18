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
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        answer = 0
        w, h = (int(input()) for _ in range(2))
        grid = [["!" for _ in range(w + 2)]] + [["!"] + list(input()) + ["!"] for _ in range(h)] + [["!" for _ in range(w + 2)]]
        eprint(*grid, sep="\n")
        fire_spread_time = [[INF for _ in range(w + 2)] for _ in range(h + 2)]
        escape_time = [[-1 for _ in range(w + 2)] for _ in range(h + 2)]
        queue = deque([])
        for r, c in product(range(h + 2), range(w + 2)):
            if grid[r][c] == "*":
                queue.append((r, c))
                fire_spread_time[r][c] = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in DELTA:
                nr, nc = r + dr, c + dc
                if not is_inbound(nr, h + 2, nc, w + 2):
                    continue
                if fire_spread_time[nr][nc] != INF:
                    continue
                if grid[nr][nc] == "#":
                    continue
                if grid[nr][nc] == "!":
                    continue
                fire_spread_time[nr][nc] = min(fire_spread_time[nr][nc], fire_spread_time[r][c] + 1)
                queue.append((nr, nc))
        #eprint(*fire_spread_time, sep="\n")
        queue.clear()
        for r, c in product(range(h + 2), range(w + 2)):
            if grid[r][c] == "@":
                queue.append((r, c))
                escape_time[r][c] = 0
        answer = INF
        escape_complete = False
        while queue:
            r, c = queue.popleft()
            if escape_complete:
                break
            for dr, dc in DELTA:
                nr, nc = r + dr, c + dc
                if not is_inbound(nr, h + 2, nc, w + 2):
                    continue
                if escape_time[nr][nc] != -1:
                    continue
                if grid[nr][nc] == "#":
                    continue
                if grid[nr][nc] == "!":
                    answer = escape_time[r][c] + 1
                    escape_complete = True
                    break
                if fire_spread_time[nr][nc] <= escape_time[r][c] + 1:
                    continue
                escape_time[nr][nc] = escape_time[r][c] + 1
                queue.append((nr, nc))
        #eprint(*escape_time, sep="\n")
        if escape_complete:
            answers.append(f"{answer}")
        else:
            answers.append("IMPOSSIBLE")
    print(*answers, sep="\n")
