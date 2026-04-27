from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        grid = [[int(input()) for _ in range(n * n)] for _ in range(n * n)]
        row = [[1] + [0 for _ in range(n * n)] for _ in range(n * n)]
        col = [[1] + [0 for _ in range(n * n)] for _ in range(n * n)]
        square = [[1] + [0 for _ in range(n * n)] for _ in range(n * n)]
        for r in range(n * n):
            for c in range(n * n):
                if not 1 <= grid[r][c] <= n * n:
                    continue
                row[r][grid[r][c]] += 1
                col[c][grid[r][c]] += 1
        for r1, c1 in product(range(n), repeat=2):
            for r2, c2 in product(range(n), repeat=2):
                if not 1 <= grid[r1 * n + r2][c1 * n + c2] <= n * n:
                    continue
                square[r1 * n + c1][grid[r1 * n + r2][c1 * n + c2]] += 1
        is_valid = all(all(i == 1 for i in v) for v in row) & all(all(i == 1 for i in v) for v in col) & all(
            all(i == 1 for i in v) for v in square)
        answer = f"Case #{h + 1}: {'Yes' if is_valid else 'No'}"
        answers[h] = answer
    print(answers)