from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000


def is_inbound(pos_x, pos_y, size_x, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens) if tokens else ""
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        directions = [(1, 0), (-1, 0)]
        current_dir = 0
        n = int(input())
        grid = [[0 for _ in range(n)] for _ in range(n)]
        queue = deque([(0, 0)])
        grid[0][0] = 1
        fill_count = 1
        while queue:
            if fill_count == n * n:
                break
            cur_x, cur_y = queue.popleft()
            dx, dy = directions[current_dir]
            next_x, next_y = cur_x + dx, cur_y + dy
            if not is_inbound(next_x, next_y, n, n):
                current_dir += 1
                current_dir %= 2
                dx, dy = directions[current_dir]
                next_x, next_y = cur_x, cur_y + 1
            grid[next_y][next_x] = grid[cur_y][cur_x] + 1
            queue.append((next_x, next_y))
            fill_count += 1
        answer = "\n".join(" ".join(map(str, x)) for x in grid)
        answers.append(f"{answer}")
    print(*answers, sep="\n")