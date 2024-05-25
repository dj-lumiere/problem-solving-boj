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
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        a = list(map(int, input().decode()))
        b = list(map(int, input().decode()))
        a_and_b = [i & j for i, j in zip(a, b)]
        a_or_b = [i | j for i, j in zip(a, b)]
        a_xor_b = [i ^ j for i, j in zip(a, b)]
        not_a = [1 ^ i for i, j in zip(a, b)]
        not_b = [1 ^ j for i, j in zip(a, b)]
        result = ["".join(map(str, a_and_b)), "".join(map(str, a_or_b)), "".join(map(str, a_xor_b)), "".join(map(str, not_a)), "".join(map(str, not_b))]
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(answers)