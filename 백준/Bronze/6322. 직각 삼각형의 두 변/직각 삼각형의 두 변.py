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
    print = lambda x: write(1, "\n\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 0
    answers = ["" for _ in range(0)]
    tokens2 = list(map(int, tokens))
    for _ in range(3):
        tokens2.pop()
    tokens2.reverse()
    t = len(tokens2) // 3
    for hh in range(t):
        a, b, c = tokens2.pop(), tokens2.pop(), tokens2.pop()
        answer = f"Triangle #{hh + 1}\n"
        if a == -1:
            result = (c ** 2 - b ** 2) ** .5 if c > b else -1
            if result == -1:
                answer += "Impossible."
            else:
                answer += f"a = {result:.3f}"
        if b == -1:
            result = (c ** 2 - a ** 2) ** .5 if c > a else -1
            if result == -1:
                answer += "Impossible."
            else:
                answer += f"b = {result:.3f}"
        if c == -1:
            result = (a ** 2 + b ** 2) ** .5
            if result == -1:
                answer += "Impossible."
            else:
                answer += f"c = {result:.3f}"
        answers.append(f"{answer}")
    print(answers)