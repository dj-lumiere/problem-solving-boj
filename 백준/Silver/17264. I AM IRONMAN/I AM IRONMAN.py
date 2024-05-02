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
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        p = int(input())
        w = int(input())
        l = int(input())
        g = int(input())
        sure_win = set()
        for _ in range(p):
            name, win = input().decode(), input().decode()
            if win == "W":
                sure_win.add(name)
        score = 0
        for _ in range(n):
            name = input().decode()
            if name in sure_win:
                score += w
            else:
                score -= l
            if score >= g:
                break
            if score < 0:
                score = 0
        answer = "I AM NOT IRONMAN!!" if score >= g else "I AM IRONMAN!!"
        answers[h] = answer
    print(answers)