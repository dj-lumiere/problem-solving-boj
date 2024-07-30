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


def convert_to_heart(n):
    is_negative = n < 0
    if n < 0:
        n *= -1
    digits = []
    while n != 0:
        n, digit = divmod(n, 3)
        digits.append(digit)
    digits.append(0)
    for i, v in enumerate(digits):
        if i + 1 == len(digits):
            break
        if digits[i] >= 2:
            digits[i] -= 3
            digits[i + 1] += 1
    if is_negative:
        digits = [-v for v in digits]
    if digits[-1] == 0:
        digits.pop()
    if not digits:
        digits.append(0)
    return ''.join(map(lambda x: "-" if x < 0 else f"{x}", reversed(digits)))

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    for hh in range(t):
        n = int(input())
        answer = convert_to_heart(n)
        answers.append(f"{answer}")
    print(*answers, sep="\n")