from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
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


def selection_sort(a, n, b):
    for last in range(n, 1, -1):
        i = a[:last + 1].index(max(a[:last + 1]))
        if a == b:
            return 1
        if last != i:
            a[i], a[last] = a[last], a[i]
            if a == b:
                return 1
    return 0


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        a = [0] + [int(input()) for _ in range(n)]
        b = [0] + [int(input()) for _ in range(n)]
        answer = selection_sort(a, n, b)
        answers.append(f"{answer}")
    print(answers)