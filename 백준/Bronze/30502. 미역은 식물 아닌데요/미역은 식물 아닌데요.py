from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
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
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep="\n", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        m = int(input())
        properties = [[-1, -1] for _ in range(n + 1)]
        properties[0] = [0, 0]
        for _ in range(m):
            a, b, c = int(input()), input().decode(), int(input())
            if b == "P":
                properties[a][0] = c
            elif b == "M":
                properties[a][1] = c
        eprint(properties)
        is_plant = sum(i == 1 and j == 0 for i, j in properties)
        is_not_plant = sum(i == 0 or j == 1 for i, j in properties)
        possibly_plant = sum((i == 1 and j == -1) or (i == -1 and j == 0) or i == j == -1 for i, j in properties)
        answer = f"{is_plant} {is_plant + possibly_plant}"
        answers.append(f"{answer}")
    print(*answers)