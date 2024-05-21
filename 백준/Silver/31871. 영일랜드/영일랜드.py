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
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        distances = [[10 ** 18 for _ in range(n + 1)] for _ in range(n + 1)]
        m = int(input())
        for _ in range(m):
            start, end, distance = [int(input()) for _ in range(3)]
            if start == end:
                distance = 10 ** 18
                continue
            distances[start][end] = max(distances[start][end], distance) if distances[start][end] != 10**18 else distance
        answer = -1
        for path in permutations(range(1, n + 1)):
            answer_sub = 0
            for i, j in zip([0] + list(path), list(path) + [0]):
                answer_sub += distances[i][j]
            if answer_sub >= 10 ** 18:
                continue
            answer = max(answer, answer_sub)
        answers.append(f"{answer}")
    print(answers)