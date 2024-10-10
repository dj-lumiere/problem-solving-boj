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
        flag = [input() for i in range(6)]
        min_changes = INF
        for top_color, middle_color, bottom_color in product(ascii_uppercase, repeat=3):
            if top_color == middle_color:
                continue
            desired_flag1 = [[top_color] * 9 for _ in range(2)] + [[middle_color] * 9 for _ in range(2)] + [
                [bottom_color] * 9 for _ in range(2)]
            desired_flag2 = [[top_color] * 3 + [middle_color] * 3 + [bottom_color] * 3 for _ in range(6)]
            changes1 = 0
            changes2 = 0
            for i, j in product(range(6), range(9)):
                if flag[i][j] != desired_flag1[i][j]:
                    changes1 += 1
                if flag[i][j] != desired_flag2[i][j]:
                    changes2 += 1
            min_changes = min(changes1, changes2, min_changes)
        answers.append(min_changes)
    print(*answers, sep="\n")