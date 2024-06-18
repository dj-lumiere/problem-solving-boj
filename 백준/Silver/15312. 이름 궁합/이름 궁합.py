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
    strokes = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    for hh in range(t):
        a = input()
        b = input()
        name_zip = []
        for i, j in zip(a, b):
            name_zip.extend([i, j])
        table = [[] for _ in range(len(name_zip) - 1)]
        table[0] = [strokes[i - ord("A")] for i in name_zip]
        for i in range(len(name_zip) - 1):
            if i == 0:
                continue
            table[i] = [(j + k) % 10 for j, k in zip(table[i - 1], table[i - 1][1:])]
        answer = "".join(map(str, table[-1]))
        answers.append(f"{answer}")
    print(answers)