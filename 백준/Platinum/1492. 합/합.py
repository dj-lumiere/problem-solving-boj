from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
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
from datetime import datetime, time, timedelta

getcontext().prec = 1000


def powered_sum(n, d):
    if n <= d + 2:
        return sum(pow(i, d, MOD) for i in range(n + 1)) % MOD
    smaller_sum = [0]
    for i in range(1, d + 3):
        smaller_sum.append(smaller_sum[-1] + pow(i, d, MOD))
    numerator_accumulate = [n]
    for i in range(1, d + 3):
        numerator_accumulate.append(numerator_accumulate[-1] * (n - i) % MOD)
    numerator_inverse = [pow(numerator_accumulate[-1], -1, MOD)]
    for i in reversed(range(1, d + 3)):
        numerator_inverse.append(numerator_inverse[-1] * (n - i) % MOD)
    numerator_inverse.reverse()
    numerator_sub_inverse = [i * j % MOD for i, j in zip(numerator_accumulate, numerator_inverse[1:])]
    denominator_sub = list(range(-d - 1, 0)) + list(range(1, d + 2))
    denominator_accumulate = [1]
    for v in denominator_sub:
        denominator_accumulate.append(denominator_accumulate[-1] * v % MOD)
    denominator_accumulate_inverse = [pow(denominator_accumulate[-1], -1, MOD)]
    for i, v in enumerate(reversed(denominator_sub)):
        denominator_accumulate_inverse.append(denominator_accumulate_inverse[-1] * v % MOD)
    denominator_accumulate_inverse.reverse()
    denominators = [i * j % MOD for i, j in zip(denominator_accumulate, denominator_accumulate_inverse[d + 1:])]
    numerators = [numerator_accumulate[-1] * numerator_inverse[0] * v % MOD for v in numerator_sub_inverse]
    coefficients = [i * j % MOD for i, j in zip(numerators, denominators)]
    return sum(i * j % MOD for i, j in zip(coefficients, smaller_sum[1:])) % MOD


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, sep="\n": write(2, (sep.join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n, k = int(input()), int(input())
        answer = powered_sum(n, k) % MOD
        answers.append(f"{answer}")
    print(answers)