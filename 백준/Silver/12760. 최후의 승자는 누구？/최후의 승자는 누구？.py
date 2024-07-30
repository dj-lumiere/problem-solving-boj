from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
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
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        m = int(input())
        score = [0 for _ in range(n+1)]
        cards = [[]]+[sorted([int(input()) for _ in range(m)]) for _ in range(n)]
        for _ in range(m):
            battle = [0] + [cards[i].pop() for i in range(1, n+1)]
            for i, v in enumerate(battle):
                if v == max(battle):
                    score[i] += 1
        result = []
        for i, v in enumerate(score):
            if v == max(score):
                result.append(i)
        answer = " ".join(map(str, result))
        answers.append(f"{answer}")
    print(*answers, sep="\n")