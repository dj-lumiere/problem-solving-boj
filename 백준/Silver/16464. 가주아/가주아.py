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

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep="\n", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    possible_pairs = []
    for i in range(2, 10 ** 9):
        start = i * (i + 1) // 2
        if start >= 10 ** 9:
            break
        if start % 2 == 0:
            possible_pairs.append((1, i, i, start))
        elif (start + i) % 2 == 0:
            possible_pairs.append((2, i + 1, i, start + i))
    for hh in range(t):
        n = int(input())
        answer = "GoHanGang"
        if n % 2 == 1:
            answer = "Gazua"
        else:
            for s, e, c, x in possible_pairs:
                offset, mod = divmod(n - x, c)
                if offset < 0:
                    break
                if mod == 0 and e + offset < n:
                    answer = "Gazua"
                    break
        answers.append(f"{answer}")
    print(*answers)