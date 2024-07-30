from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        grid = [[int(input()) for _ in range(5)] for _ in range(5)]
        r, c = [int(input()) for _ in range(2)]
        distance = [[0 for _ in range(5)] for _ in range(5)]
        queue = deque()
        distance[r][c] = 1
        queue.appendleft((r, c))
        answer = -1
        while queue:
            y, x = queue.popleft()
            if grid[y][x] == 1:
                answer = distance[y][x] - 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < 5 and 0 <= nx < 5):
                    continue
                if grid[ny][nx] == -1:
                    continue
                if distance[ny][nx] != 0:
                    continue
                distance[ny][nx] = distance[y][x] + 1
                queue.append((ny, nx))
        answers.append(f"{answer}")
    print(answers)