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
    t = 1
    for hh in range(t):
        S_year, S_month, S_day = (int(input()) for _ in range(3))
        E_year, E_month, E_day = (int(input()) for _ in range(3))
        work_days = (E_year - S_year) * 360 + (E_month - S_month) * 30 + (E_day - S_day)
        work_month = (E_year - S_year) * 12 + (E_month - S_month) + -(E_day - S_day < 0)
        work_year = work_month // 12
        monthly_vacation_days = min(work_month, 36)
        yearly_vacation_days = sum(i // 2 + 15 for i in range(work_year))
        answer = f"{yearly_vacation_days} {monthly_vacation_days}\n{work_days}days"
        answers.append(f"{answer}")
    print(*answers, sep="\n")