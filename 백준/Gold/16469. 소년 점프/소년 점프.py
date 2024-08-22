from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        r, c = int(input()), int(input())
        grid = [list(map(int, input())) for _ in range(r)]
        times = [[[] for _ in range(c)] for _ in range(r)]
        villains = []
        for _ in range(3):
            y, x = int(input()), int(input())
            time_grid = [[0 for _ in range(c)] for _ in range(r)]
            queue = deque([(x - 1, y - 1)])
            time_grid[y - 1][x - 1] = 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in DELTA:
                    nx, ny = x + dx, y + dy
                    if not is_inbound(nx, c, ny, r):
                        continue
                    if grid[ny][nx] != 0:
                        continue
                    if time_grid[ny][nx] != 0:
                        continue
                    time_grid[ny][nx] = time_grid[y][x] + 1
                    queue.append((nx, ny))
            for y, x in product(range(r), range(c)):
                if time_grid[y][x] != 0:
                    times[y][x].append(time_grid[y][x] - 1)
        total_time = [[max(times[y][x]) if len(times[y][x]) == 3 else INF for x in range(c)] for y in range(r)]
        min_time = min(total_time[y][x] for y, x in product(range(r), range(c)))
        min_count = sum(total_time[y][x] == min_time for y, x in product(range(r), range(c)))
        answer = f"{min_time}\n{min_count}" if min_time != INF else "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
