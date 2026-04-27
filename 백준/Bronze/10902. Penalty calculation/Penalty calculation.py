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
    answers = ["" for _ in range(t)]
    for hh in range(t):
        n = int(input())
        answer = 0
        s_list = []
        t_list = []
        for _ in range(n):
            t, s = int(input()), int(input())
            s_list.append(s)
            t_list.append(t)
        max_s = s_list.index(max(s_list))
        answer = 0 if s_list[max_s] == 0 else t_list[max_s] + (max_s) * 20
        answers[hh] = f"{answer}"
    print(answers)