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
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        score = [0 for _ in range(n + 1)]
        for _ in range(n * (n - 1) // 2):
            a, b, c, d = [int(input()) for _ in range(4)]
            if c > d:
                score[a] += 3
            elif c < d:
                score[b] += 3
            else:
                score[a] += 1
                score[b] += 1
        sorted_score = sorted(score, reverse=True)
        rank = {}
        for i1, v1 in enumerate(sorted_score, start=1):
            if v1 in rank:
                continue
            rank[v1] = i1
        answer = [rank[v] for v in score[1:]]
        answers[h] = "\n".join(map(str, answer))
    print(answers)