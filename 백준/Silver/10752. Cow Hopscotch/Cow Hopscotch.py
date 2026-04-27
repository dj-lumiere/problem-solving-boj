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
        r = int(input())
        c = int(input())
        grid = [list(input().decode()) for _ in range(r)]
        table = [[[0, 0] for _ in range(c)] for _ in range(r)]
        if grid[0][0] == "R":
            table[0][0][0] = 1
        else:
            table[0][0][1] = 1
        for y, x in product(range(r), range(c)):
            if x == y == 0:
                continue
            for x2, y2 in product(range(x), range(y)):
                if grid[y][x] == "B":
                    table[y][x][1] += table[y2][x2][0]
                elif grid[y][x] == "R":
                    table[y][x][0] += table[y2][x2][1]
        answer = sum(table[-1][-1])
        answers.append(f"{answer}")
    print(answers)