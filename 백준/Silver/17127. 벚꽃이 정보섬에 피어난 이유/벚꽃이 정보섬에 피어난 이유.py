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
with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        answer = 0
        for seperations in combinations(range(1, n), r=3):
            seperations = [0] + list(seperations) + [n]
            groups = [[] for _ in range(4)]
            for i, v in enumerate(a):
                for j, (sep1, sep2) in enumerate(zip(seperations, seperations[1:])):
                    if sep1 <= i < sep2:
                        groups[j].append(v)
                        break
            answer_sub = sum(reduce(lambda x, y: x * y, a) for a in groups)
            answer = max(answer, answer_sub)
        answers.append(f"{answer}")
    print(answers)