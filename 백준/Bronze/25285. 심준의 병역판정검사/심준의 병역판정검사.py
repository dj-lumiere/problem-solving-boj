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
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        h, w = int(input()), int(input())
        bmi = w / (h / 100) / (h / 100)
        answer = 0
        if h < 140.1:
            answer = 6
        elif 140.1 <= h < 146:
            answer = 5
        elif 146 <= h < 159:
            answer = 4
        elif 159 <= h < 161:
            if 16 <= bmi < 35:
                answer = 3
            else:
                answer = 4
        elif 161 <= h < 204:
            if 20 <= bmi < 25:
                answer = 1
            elif 18.5 <= bmi < 30:
                answer = 2
            elif 16 <= bmi < 35:
                answer = 3
            else:
                answer = 4
        else:
            answer = 4
        answers.append(f"{answer}")
print(*answers, sep="\n")
