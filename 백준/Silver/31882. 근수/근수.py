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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        s = list(input().decode()) + ["1"]
        two_sequence_length = []
        stack = 0
        for i, v in enumerate(s):
            if v != "2" and stack != 0:
                two_sequence_length.append(stack)
                stack = 0
            elif v == "2":
                stack += 1
        answer = 0
        for v in two_sequence_length:
            answer += v * v * (v + 1) // 2 - v * (v + 1) * (2 * v + 1) // 6 + v * (v + 1) // 2
        answers.append(f"{answer}")
    print(answers)