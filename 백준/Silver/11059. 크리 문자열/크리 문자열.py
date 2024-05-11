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
        n = list(map(int, input().decode()))
        n_sum = [0]
        for i, v in enumerate(n):
            if i == 0:
                n_sum.append(v)
                continue
            n_sum.append(n_sum[-1]+v)
        answer = 0
        for i in range(1, len(n) // 2 + 1):
            for j in range(len(n) - 2 * i + 1):
                left_sum = n_sum[i+j]-n_sum[j]
                right_sum = n_sum[2*i+j]-n_sum[i+j]
                if left_sum == right_sum:
                    answer = 2 * i
                    continue
        answers[hh] = f"{answer}"
    print(answers)