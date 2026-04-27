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
    t = 0
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        pass
    while True:
        t += 1
        n = int(input())
        if n == 0:
            break
        names = []
        grid = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            name = input().decode()
            names.append(name)
            for j in range(n - 1):
                is_nasty = input().decode() == "N"
                grid[i - 1 - j][i] = is_nasty
        answer = f"Group {t}\n"
        nasty_count = 0
        for i in range(n):
            for j in range(i-1, i-1-n, -1):
                if grid[j][i]:
                    answer += f"{names[j]} was nasty about {names[i]}\n"
                    nasty_count += 1
        if not nasty_count:
            answer += "Nobody was nasty\n"
        answers.append(f"{answer}")
    print(answers)