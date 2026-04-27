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
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        if n == 1:
            answers[h] = "*"
            continue
        grid = [[" " for _ in range(4 * n - 3)] for _ in range(4 * n - 1)]
        grid[0][-1] = "*"
        draw = [4 * n - 4, 4 * n - 2, 4 * n - 4, 4 * n - 4]
        current_position = (4 * n - 4, 0)
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(n):
            for j, (x, y) in zip(draw, direction):
                for k in range(j):
                    current_position = (current_position[0] + x, current_position[1] + y)
                    grid[current_position[1]][current_position[0]] = "*"
            draw = [i - 4 for i in draw]
            if i == 0:
                draw[0] += 2
        answer = "\n".join("".join(x).strip() for x in grid)
        answers[h] = answer
    print(answers)