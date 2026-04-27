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
        n = int(input())
        grid = [list(input().decode()) for _ in range(n)]
        answer = "ongoing"
        for i, j in product(range(n-2), range(n)):
            if grid[i][j] == grid[i+1][j] == grid[i+2][j] != ".":
                answer = grid[i][j]
                break
        for i, j in product(range(n-2), range(n)):
            if grid[j][i] == grid[j][i+1] == grid[j][i+2] != ".":
                answer = grid[j][i]
                break
        for i, j in product(range(n-2), repeat=2):
            if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] != ".":
                answer = grid[i][j]
                break
        for i, j in product(range(n-2), repeat=2):
            if grid[i+2][j] == grid[i+1][j+1] == grid[i][j+2] != ".":
                answer = grid[i+1][j+1]
                break
        answers.append(f"{answer}")
    print(answers)