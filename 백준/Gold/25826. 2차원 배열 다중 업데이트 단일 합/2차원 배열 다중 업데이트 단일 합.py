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
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat
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
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        m = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        grid_rectangle = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for _ in range(m):
            op = int(input())
            if op == 1:
                y1, x1, y2, x2, k = (int(input()) for _ in range(5))
                grid_rectangle[y2 + 1][x2 + 1] += k
                grid_rectangle[y1][x1] += k
                grid_rectangle[y2 + 1][x1] -= k
                grid_rectangle[y1][x2 + 1] -= k
            elif op == 2:
                y1, x1, y2, x2 = (int(input()) for _ in range(4))
                for x, y in product(range(1, n + 1), range(n + 1)):
                    grid_rectangle[y][x] += grid_rectangle[y][x - 1]
                for x, y in product(range(n + 1), range(1, n + 1)):
                    grid_rectangle[y][x] += grid_rectangle[y - 1][x]
                answer = sum(
                    grid[y][x] + grid_rectangle[y][x] for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1)))
                answers.append(f"{answer}")
print(*answers, sep="\n")
