from array import array
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
        n = int(input())
        w = [int(input()) for _ in range(n)]
        sum_w = [0]
        for v in w:
            sum_w.append(sum_w[-1] + v)
        possible_pair = (INF, -INF)
        for start, end in product(range(n), range(1, n + 1)):
            if (end - start) < 2:
                continue
            target_w = sum_w[start] + (sum_w[end] - sum_w[start]) // 2
            target_index = bisect_left(sum_w, target_w)
            diffs = []
            for i in range(-1, 2):
                target_index2 = target_index + i
                left_persons = target_index2 - start
                right_persons = end - target_index2
                if not (left_persons > 0 and right_persons > 0):
                    continue
                left_sum = sum_w[target_index2] - sum_w[start]
                right_sum = sum_w[end] - sum_w[target_index2]
                diffs.append((abs(right_sum - left_sum), -(left_sum + right_sum)))
            possible_pair = min(*diffs, possible_pair)
        answer = -possible_pair[1]
        answers.append(answer)
    print(*answers, sep="\n")