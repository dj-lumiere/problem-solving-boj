from sys import stdin
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000


def comb(n, r, factorials, inverse_factorials):
    if n < r:
        return 0
    return factorials[n] * inverse_factorials[r] * inverse_factorials[n - r] % MOD


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 998244353
    t = 1
    for hh in range(t):
        N = int(input())
        sets = []
        factorials = [1]
        inverse_factorials = []
        result = [0] * (N + 1)
        for i in range(1, 10 ** 6 + 1):
            factorials.append(factorials[-1] * i % MOD)
        inverse_factorials.append(pow(factorials[-1], MOD - 2, MOD))
        for i in range(10 ** 6, 0, -1):
            inverse_factorials.append(inverse_factorials[-1] * i % MOD)
        inverse_factorials.reverse()
        for _ in range(N):
            size = int(input())
            s = [int(input()) for _ in range(size)]
            sets.extend(s)
        frequencies = Counter(sets)
        for v in frequencies.values():
            for i in range(1, v + 1):
                result[i] += comb(v, i, factorials, inverse_factorials)
                result[i] %= MOD
        answer = "\n".join(map(str, result[1:]))
        answers.append(f"{answer}")
    print(*answers)
