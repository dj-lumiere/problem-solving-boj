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
    answers = ["" for _ in range(t)]
    MOD = 998244353
    for hh in range(t):
        n, m = int(input()), int(input())
        grid = [[0 for _ in range(m)]] + [[int(input()) for _ in range(m)] for _ in range(n)] + [[0 for _ in range(m)]]
        min_fuel = 100000000000000
        for moves in product([(-1, 1), (0, 1), (1, 1)], repeat=n + 1):
            for i in range(m):
                fuel_sub = 0
                current_x = i
                current_y = 0
                prev_dx, prev_dy = -2, -2
                for dx, dy in moves:
                    next_x = current_x + dx
                    next_y = current_y + dy
                    if not 0 <= next_x < m:
                        fuel_sub = 100000000000000
                        break
                    if prev_dx == dx and prev_dy == dy:
                        fuel_sub = 100000000000000
                        break
                    fuel_sub += grid[next_y][next_x]
                    current_x, current_y = next_x, next_y
                    prev_dx, prev_dy = dx, dy
                eprint(current_x, current_y, fuel_sub)
                min_fuel = min(fuel_sub, min_fuel)
        answer = min_fuel
        answers[hh] = f"{answer}"
    print(answers)