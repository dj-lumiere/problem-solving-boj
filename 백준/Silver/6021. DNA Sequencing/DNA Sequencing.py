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
        m = int(input())
        f = int(input())
        bulls = [input().decode() for _ in range(m)]
        cows = [input().decode() for _ in range(f)]
        bobines = cows[:]+bulls[:]
        answer = [[0 for i in cows] for j in bulls]
        for a, i in enumerate(cows):
            for b, j in enumerate(bulls):
                for c, k in enumerate(bobines):
                    if a == c or f + b == c:
                        continue
                    for i2, j2, k2 in zip(i, j, k):
                        if k2 != i2 and k2 != j2:
                            break
                    else:
                        answer[b][a] += 1
        answers[h] = "\n".join(" ".join(map(str, x)) for x in answer)
    print(answers)