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
setrecursionlimit(100000)
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
        n = int(input())
        q = int(input())
        k2 = int(input())
        a = [0] + [int(input()) for _ in range(n)]


        def select(a, p, r, q):
            if p == r: return a[p]
            t = partition(a, p, r)
            k = t - p + 1
            if q < k:
                return select(a, p, t - 1, q)
            elif q == k:
                return a[t]
            return select(a, t + 1, r, q - k)


        def partition(a, p, r):
            global k2
            x = a[r]
            i = p - 1
            for j in range(p, r):
                if a[j] <= x:
                    i += 1
                    if k2 > 0:
                        a[i], a[j] = a[j], a[i]
                        k2 -= 1
            if i + 1 != r:
                if k2 > 0:
                    a[i + 1], a[r] = a[r], a[i + 1]
                    k2 -= 1
            return i + 1


        select(a, 1, len(a) - 1, q)
        answer = " ".join(map(str, a[1:])) if k2 == 0 else "-1"
        answers[h] = f"{answer}"
    print(answers)