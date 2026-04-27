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

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 10 ** 9
    answers = ["" for _ in range(0)]
    for hh in range(t):
        p, e, i, d = [int(input()) for _ in range(4)]
        if p == e == i == d == -1:
            break
        result = ((-p % 23) * pow(28 * 33, -1, 23) * 28 * 33 + (-e % 28) * pow(23 * 33, -1, 28) * 23 * 33 + (
                -i % 33) * pow(23 * 28, -1, 33) * 23 * 28) % 21252 + d
        answer = f"Case {hh + 1}: the next triple peak occurs in {21252 - result} days."
        answers.append(f"{answer}")
    print(answers)