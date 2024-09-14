from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000


def get_total_bill(x):
    if x <= 100:
        return 2 * x
    if x <= 10000:
        return 3 * (x - 100) + 2 * 100
    if x <= 1000000:
        return 5 * (x - 10000) + 3 * (10000 - 100) + 2 * 100
    return 7 * (x - 1000000) + 5 * (1000000 - 10000) + 3 * (10000 - 100) + 2 * 100


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    DIAGONAL = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(1, t + 1):
        a, b = int(input()), int(input())
        if a == b == 0:
            break
        # find total spending
        start = 0
        end = 10 ** 9
        while start + 1 < end:
            mid = (start + end) // 2
            if get_total_bill(mid) > a:
                end = mid
            else:
                start = mid
        total_spending = start
        start = 0
        end = total_spending + 1
        # find sanggeun spending
        while start + 1 < end:
            mid = (start + end) // 2
            opponent = total_spending - mid
            eprint(opponent, mid, get_total_bill(opponent), get_total_bill(mid),
                   get_total_bill(opponent) - get_total_bill(mid))
            if get_total_bill(opponent) - get_total_bill(mid) >= b:
                start = mid
            else:
                end = mid
        sangguen_spending = start
        # find sanggeun price
        answer = get_total_bill(sangguen_spending)
        answers.append(f"{answer}")
print(*answers, sep="\n")
