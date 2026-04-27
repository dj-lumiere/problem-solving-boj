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
    for hh in range(t):
        n = int(input())
        m = int(input())
        operation = [[False for _ in range(1440)] for _ in range(n + 1)]
        stack = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, key, h, m = int(input()), input().decode(), int(input()), int(input())
            if key == "START":
                stack[a].append(h * 60 + m)
            elif key == "STOP":
                start, end = stack[a].pop(), h * 60 + m
                operation[a][start:end] = [True] * (end - start)
        result = []
        for i in operation[1:]:
            operation_time = sum(i)
            h, m = divmod(operation_time, 60)
            result.append(f"{h} {m}")
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(answers)