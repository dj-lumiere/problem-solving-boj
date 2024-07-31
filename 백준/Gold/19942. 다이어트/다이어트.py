from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens) if tokens else ""
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        N = int(input())
        mp, mf, ms, mv = [int(input()) for _ in range(4)]
        ingredients = [[int(input()) for _ in range(5)] for _ in range(N)]
        min_cost = INF
        min_combination = [INF for _ in range(N)]
        for mask in range(1, 1 << N):
            combination = [i + 1 for i, v in enumerate([mask & (1 << j) != 0 for j in range(N)]) if v]
            p = sum(v[0] for i, v in enumerate(ingredients) if mask & (1 << i) != 0)
            f = sum(v[1] for i, v in enumerate(ingredients) if mask & (1 << i) != 0)
            s = sum(v[2] for i, v in enumerate(ingredients) if mask & (1 << i) != 0)
            v2 = sum(v[3] for i, v in enumerate(ingredients) if mask & (1 << i) != 0)
            c = sum(v[4] for i, v in enumerate(ingredients) if mask & (1 << i) != 0)
            if p >= mp and f >= mf and s >= ms and v2 >= mv:
                if c < min_cost:
                    min_cost = c
                    min_combination = combination
                elif c == min_cost:
                    min_combination = min(combination, min_combination)
        answer = ""
        if min_cost != INF:
            answer += f"{min_cost}\n" + " ".join(map(str, min_combination))
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers)