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
        n = list(map(lambda x: ord(x) - ord("A"), input().decode()))
        if n == [ord("#") - ord("A")]:
            break
        answer = "That music is beautiful."
        for i, j in zip(n, n[1:]):
            if j - i in [2, 4, 6] or j + 7 - i in [2, 4, 6]:
                continue
            answer = "Ouch! That hurts my ears."
            break
        answers.append(f"{answer}")
    print(answers)