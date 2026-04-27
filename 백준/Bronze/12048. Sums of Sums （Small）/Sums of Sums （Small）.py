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
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        q = int(input())
        answer = [f"Case #{h + 1}:"]
        numbers = [int(input()) for _ in range(n)]
        numbers_sum = [0]
        for i, v in enumerate(numbers):
            numbers_sum.append(numbers_sum[-1] + v)
        possible_sums = []
        for i, j in product(range(n + 1), repeat=2):
            if i > j:
                possible_sums.append(numbers_sum[i] - numbers_sum[j])
        eprint(len(possible_sums))
        possible_sums.sort()
        possible_sums_sums = [0]
        for i, v in enumerate(possible_sums):
            possible_sums_sums.append(possible_sums_sums[-1] + v)
        for _ in range(q):
            a, b = int(input()), int(input())
            answer.append(f"{possible_sums_sums[b] - possible_sums_sums[a - 1]}")
        answers[h] = "\n".join(answer)
    print(answers)