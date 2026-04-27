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
        a, p = int(input()), int(input())
        d = [a]
        has_item = {a}
        latest_cycle = -1
        answer = -1
        for _ in range(10000):
            d.append(sum(map(lambda x: int(x)**p, str(d[-1]))))
            if d[-1] in has_item:
                latest_cycle = d[-1]
                answer = d.index(latest_cycle)
                break
            has_item.add(d[-1])
        answers.append(f"{answer}")
    print(answers)