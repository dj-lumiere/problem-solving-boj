from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
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


def is_inbound(pos_x, size_x, pos_y, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        c, r = int(input()), int(input())
        grid = [list(input().decode()) for _ in range(r)]
        distance = [[0 for _ in range(c)] for _ in range(r)]
        start = (0, 0)
        end = (0, 0)
        for y, x in product(range(r), range(c)):
            if grid[y][x] == "K":
                start = (x, y)
                grid[y][x] = "*"
            if grid[y][x] == "H":
                end = (x, y)
        queue = deque([start])
        while queue:
            current_x, current_y = queue.popleft()
            if grid[current_y][current_x] == "H":
                continue
            for dx, dy in [(-1, 2), (1, 2), (-1, -2), (1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]:
                next_x, next_y = current_x + dx, current_y + dy
                if not is_inbound(next_x, c, next_y, r):
                    continue
                if grid[next_y][next_x] == "*":
                    continue
                grid[next_y][next_x] = "*"
                distance[next_y][next_x] = distance[current_y][current_x] + 1
                queue.append((next_x, next_y))
        answer = distance[end[1]][end[0]]
        answers.append(f"{answer}")
    print(answers)