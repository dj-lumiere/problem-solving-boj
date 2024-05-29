from bisect import bisect_left
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

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    beat = [*range(1, 16)] + [*range(14, 1, -1)]
    for hh in range(t):
        _, preference, max_geo_distance = input().decode(), input().decode(), int(input())
        n = int(input())
        pairings = []
        for _ in range(n):
            name, gender, geo_distance = input().decode(), input().decode(), int(input())
            if gender in preference and geo_distance <= max_geo_distance:
                pairings.append(name)
        pairings.sort()
        answer = "No one yet"
        if pairings:
            answer = "\n".join(pairings)
        answers.append(f"{answer}")
    print(answers)