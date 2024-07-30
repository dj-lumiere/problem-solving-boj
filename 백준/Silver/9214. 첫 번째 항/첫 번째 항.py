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

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    for hh in range(t):
        n = input().decode()
        if n == "0":
            break
        result = [n]
        while True:
            if len(result[-1]) % 2 == 1:
                break
            is_invalid = False
            for i, j in zip(result[-1][1::2], result[-1][3::2]):
                if i == j:
                    is_invalid = True
                    break
            if is_invalid:
                break
            result_sub = ""
            for i, j in zip(result[-1][::2], result[-1][1::2]):
                result_sub += j * int(i)
            result.append(result_sub)
            if result[-1] == result[-2]:
                break
            if len(result_sub) % 2 == 1:
                break
        answer = f"Test {hh + 1}: {result[-1]}"
        answers.append(f"{answer}")
    print(answers)