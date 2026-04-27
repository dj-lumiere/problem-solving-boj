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
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 998244353
    for hh in range(t):
        pass
    while True:
        n = input().decode()
        if n == "0":
            break
        m = input().decode()
        n *= (len(m) + len(n) - 1) // len(n)
        answer = ""
        for i, j in zip(n, m):
            alphabet_shifts = ord(i) - ord("A") + 1
            letter = chr((ord(j) - ord("A") + alphabet_shifts) % 26 + ord("A"))
            answer += letter
        answers.append(f"{answer}")
    print(answers)