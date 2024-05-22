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
    t = 0
    answers = ["" for _ in range(0)]
    for hh in range(t):
        pass
    while True:
        a = [int(input()) for _ in range(6)]
        if all(i == 0 for i in a):
            break
        a.sort()
        x, y = divmod(sum(a[1:-1]), 4)
        answer = f"{x}"
        if y == 1:
            answer += ".25"
        elif y == 2:
            answer += ".5"
        elif y == 3:
            answer += ".75"
        answers.append(f"{answer}")
    print(answers)