from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

PRECOMPUTE_LIMIT = int(10 ** 4.4)
mu_i_small = [0 for _ in range(PRECOMPUTE_LIMIT + 1)]
mu_i_small[1] = 1
sum_of_i_mu_i_small = [0 for _ in range(PRECOMPUTE_LIMIT + 1)]
sum_of_i_mu_i_big = {}

for i in range(1, PRECOMPUTE_LIMIT + 1):
    for j in range(2 * i, PRECOMPUTE_LIMIT + 1, i):
        mu_i_small[j] -= mu_i_small[i]
    sum_of_i_mu_i_small[i] = sum_of_i_mu_i_small[i - 1] + mu_i_small[i] * i


def sum_of_i_mu_i(x):
    i, j = 2, 0
    if x <= PRECOMPUTE_LIMIT:
        return sum_of_i_mu_i_small[x]
    if x in sum_of_i_mu_i_big:
        return sum_of_i_mu_i_big[x]
    result = 1
    while i <= x:
        j = x // (x // i)
        result -= (j * (j + 1) - i * (i - 1)) // 2 * sum_of_i_mu_i(x // i)
        i = j + 1
    sum_of_i_mu_i_big[x] = result
    return result


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        n_over_ds = []
        lower_bound = []
        upper_bound = []
        for i in range(1, int(n ** .5) + 1):
            n_over_ds.append(i)
            n_over_ds.append(n // i)
        n_over_ds = sorted(set(n_over_ds))
        for i, j in zip(n_over_ds, n_over_ds[1:]):
            lower_bound.append(i + 1)
            upper_bound.append(j)
        lower_bound.reverse()
        upper_bound.reverse()
        lower_bound.append(1)
        upper_bound.append(1)
        sum_of_i_mu_i_lower_bound = [sum_of_i_mu_i(v - 1) for v in lower_bound]
        sum_of_i_mu_i_upper_bound = [sum_of_i_mu_i(v) for v in upper_bound]
        auxilary_terms = [v * (v + 1) ** 2 % MOD for v, l, r in zip(n_over_ds, lower_bound, upper_bound)]
        answer = sum(
            v * (r - l) % MOD for v, l, r in
            zip(auxilary_terms, sum_of_i_mu_i_lower_bound, sum_of_i_mu_i_upper_bound)) - 2
        answer %= MOD
        answers.append(f"{answer}")
    print(*answers, sep="\n")