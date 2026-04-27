from base64 import b64decode, b64encode
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
from datetime import datetime, time, timedelta

getcontext().prec = 1000

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
        n = int(input())
        sample_grid = [[False for _ in range(101)] for _ in range(101)]
        delta = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
        start = (50, 50)
        sample_grid[start[0]][start[1]] = True
        for _ in range(n):
            dir = int(input())
            dx, dy = delta[dir]
            start_x, start_y = start
            sample_grid[start_y + dy][start_x + dx] = True
            start = (start_x + dx, start_y + dy)
        m = int(input())
        result = []
        for _ in range(m):
            compare_moves = [int(input()) for _ in range(n)]
            for i in range(n):
                compare_moves2 = compare_moves[i:] + compare_moves[:i]
                compare_grid = [[False for _ in range(101)] for _ in range(101)]
                start = (50, 50)
                compare_grid[start[0]][start[1]] = True
                for dir in compare_moves2:
                    dx, dy = delta[dir]
                    start_x, start_y = start
                    compare_grid[start_y + dy][start_x + dx] = True
                    start = (start_x + dx, start_y + dy)
                if sample_grid == compare_grid:
                    result.append(compare_moves[:])
                    break
        answer = f"{len(result)}\n" + "\n".join(" ".join(map(str, v)) for v in result)
        answers.append(f"{answer}")
    print(answers)