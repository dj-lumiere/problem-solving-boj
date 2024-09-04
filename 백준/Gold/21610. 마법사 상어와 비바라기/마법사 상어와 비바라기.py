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
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
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
    DELTA = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    DIAGONAL = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        m = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]

        # Set initial clouds
        cloud = [[0 for _ in range(n)] for _ in range(n)]
        previous_cloud = [[0 for _ in range(n)] for _ in range(n)]
        cloud[-1][0] = cloud[-1][1] = cloud[-2][0] = cloud[-2][1] = 1

        for i in range(m):
            d, s = int(input()), int(input())
            clouds = [(r, c) for r, c in product(range(n), repeat=2) if cloud[r][c] == 1]
            previous_cloud = [[0 for _ in range(n)] for _ in range(n)]
            dx, dy = DELTA[d]
            # Move Cloud
            after_move = [((r + dy * s) % n, (c + dx * s) % n) for r, c in clouds]
            # Make it rain
            for r, c in after_move:
                grid[r][c] += 1
                previous_cloud[r][c] = 1
            # Copy water
            for r, c in after_move:
                for dx2, dy2 in DIAGONAL:
                    nr, nc = r + dx2, c + dy2
                    if not is_inbound(nr, n, nc, n):
                        continue
                    grid[r][c] += 1 if grid[nr][nc] else 0
            cloud = [[0 for _ in range(n)] for _ in range(n)]
            # Generate new cloud and drain water.
            for r, c in product(range(n), repeat=2):
                if grid[r][c] >= 2 and previous_cloud[r][c] != 1:
                    cloud[r][c] = 1
                    grid[r][c] -= 2
        answer = sum(sum(v) for v in grid)
        answers.append(f"{answer}")
print(*answers, sep="\n")
