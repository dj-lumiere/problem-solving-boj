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
        cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
        pairs = []
        for _ in range(n):
            a, _, _, _, _, b = [input().decode() for _ in range(6)]
            pairs.append((a, b))
        results = []
        for order in permutations(cows):
            is_valid = True
            for a, b in pairs:
                if abs(order.index(a)-order.index(b)) != 1:
                    is_valid = False
                    break
            if not is_valid:
                continue
            else:
                results.append(order)
        results.sort()
        result = results[0]
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(answers)