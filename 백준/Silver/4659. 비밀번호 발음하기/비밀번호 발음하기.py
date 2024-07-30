from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens) if tokens else ""
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    for hh in range(t):
        s = input().decode()
        if s == "end":
            break
        is_acceptable = True
        if all(i not in "aeiou" for i in s):
            is_acceptable = False
        for i, j in zip(s, s[1:]):
            if i == j and i not in ("e", "o"):
                is_acceptable = False
        for x in zip(s, s[1:], s[2:]):
            if all(i not in "aeiou" for i in x):
                is_acceptable = False
            if all(i in "aeiou" for i in x):
                is_acceptable = False
        answer = f"<{s}> {'is' if is_acceptable else 'is not'} acceptable."
        answers.append(f"{answer}")
    print(*answers, sep="\n")