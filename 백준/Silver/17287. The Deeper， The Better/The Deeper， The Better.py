from bisect import bisect_left
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
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = input().decode()
        max_score = 0
        stack = []
        for v in n:
            if v.isdigit():
                current_score = 0
                for v2 in stack:
                    if v2 == "(":
                        current_score += 1
                    if v2 == "{":
                        current_score += 2
                    if v2 == "[":
                        current_score += 3
                max_score = max(max_score, current_score)
            elif v in ("(", "{", "["):
                stack.append(v)
            elif v in (")", "}", "]"):
                stack.pop()
        answer = max_score
        answers.append(f"{answer}")
    print(answers)