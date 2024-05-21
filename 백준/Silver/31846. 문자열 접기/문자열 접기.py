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
    n = int(input())
    a = [""] + list(input().decode())
    t = int(input())
    answers = ["" for _ in range(0)]
    for hh in range(t):
        l, r = int(input()), int(input())
        substring = a[l:r + 1]
        answer = 0
        for i in range(r + 1 - l):
            sub1 = substring[:i]
            sub2 = substring[i:][::-1]
            if len(sub1) > len(sub2):
                sub2 = [""] * (len(sub1) - len(sub2)) + sub2
            elif len(sub1) < len(sub2):
                sub1 = [""] * (len(sub2) - len(sub1)) + sub1
            answer_sub = sum(i == j for i, j in zip(sub1, sub2))
            answer = max(answer_sub, answer)
        answers.append(f"{answer}")
    print(answers)