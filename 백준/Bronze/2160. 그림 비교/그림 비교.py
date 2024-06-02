from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
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
with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        pictures = [[[] for _ in range(5)]] + [[list(input()) for _ in range(5)] for _ in range(n)]
        current_min_difference = 36
        current_index = (0, 0)
        for i, j in combinations(range(1, n + 1), r=2):
            min_difference = sum(pictures[i][r][c] != pictures[j][r][c] for r, c in product(range(5), range(7)))
            if current_min_difference > min_difference:
                current_min_difference = min_difference
                current_index = (i, j)
        answer = " ".join(map(str, current_index))
        answers.append(f"{answer}")
    print(answers)