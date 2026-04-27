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
        m = int(input())
        a = [int(input()) for _ in range(n)]
        a.sort()
        a_set = set(a)
        answer_sub = []
        for _ in range(m):
            d = int(input())
            if d not in a_set:
                answer_sub_sub = -1
            else:
                answer_sub_sub = bisect_left(a, d)
            answer_sub.append(answer_sub_sub)
        answer = "\n".join(map(str, answer_sub))
        answers.append(f"{answer}")
    print(answers)