from bisect import bisect_left
from string import ascii_lowercase
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
    MOD = 11092019
    for h in range(t):
        r = int(input())
        c = int(input())
        grid = [list(map(int, input().decode())) for _ in range(r)]
        answer = 1
        for size in range(1, min(r, c) + 1):
            for x in range(c - size):
                for y in range(r - size):
                    if grid[y][x] == grid[y + size][x + size] == grid[y + size][x] == grid[y][x + size]:
                        answer = size * size + 2*size+1
        answers[h] = f"{answer}"
    print(answers)