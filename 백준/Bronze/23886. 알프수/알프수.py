from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from inspect import stack
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
    x = 1
    answers = []
    for hh in range(1, x + 1):
        X = input()
        length_X = len(X)
        ascending = int(X[0]) < int(X[1])
        current_slope = abs(int(X[1]) - int(X[0]))
        is_alpsoo = True
        for i in range(1, length_X):
            if i == 1 and not ascending:
                is_alpsoo = False
                break
            current_digit = int(X[i])
            previous_digit = int(X[i - 1])
            slope = abs(current_digit - previous_digit)
            if ascending:
                if current_digit < previous_digit:
                    ascending = False
                    current_slope = slope
                elif current_digit == previous_digit:
                    is_alpsoo = False
                    break
                elif slope != current_slope:
                    is_alpsoo = False
                    break
            else:
                if current_digit > previous_digit:
                    ascending = True
                    current_slope = slope
                elif current_digit == previous_digit:
                    is_alpsoo = False
                    break
                elif slope != current_slope:
                    is_alpsoo = False
                    break
        if ascending:
            is_alpsoo = False
        if is_alpsoo:
            print("ALPSOO")
        else:
            print("NON ALPSOO")
    print(*answers, sep="\n")