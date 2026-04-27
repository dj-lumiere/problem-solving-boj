from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

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
        candy = input().decode()
        blue_candy = [+(i == "B") for i in candy]
        blue_candy_sum = [0]
        for i, v in enumerate(blue_candy):
            if i == 0:
                blue_candy_sum.append(v)
                continue
            blue_candy_sum.append(v + blue_candy_sum[-1])
        for i, v in enumerate(blue_candy):
            if i >= len(blue_candy):
                break
            blue_candy_sum.append(v + blue_candy_sum[-1])
        answer = max(blue_candy_sum[i + len(candy) // 2] - blue_candy_sum[i] for i in range(len(candy)))
        answers[h] = f"{answer}"
    print(answers)