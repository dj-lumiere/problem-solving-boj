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
    MOD = 11092019
    for hh in range(t):
        n = int(input())
        m = int(input())
        grid = [list(input().decode()) for _ in range(n)]
        answer = n * m + 1
        for i, j, k in product(range(n + 1), repeat=3):
            if i + j + k != n or not (i > 0 and j > 0 and k > 0):
                continue
            answer_sub1 = sum([sum([grid[y][x] != "W" for x in range(m)]) for y in range(i)])
            answer_sub1 += sum([sum([grid[y][x] != "B" for x in range(m)]) for y in range(i, i + j)])
            answer_sub1 += sum([sum([grid[y][x] != "R" for x in range(m)]) for y in range(i + j, i + j + k)])
            answer = min(answer, answer_sub1)
        answers[hh] = f"{answer}"
    print(answers)