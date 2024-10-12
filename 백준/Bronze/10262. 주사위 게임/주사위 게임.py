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
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, groupby
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
        a1 = int(input())
        b1 = int(input())
        a2 = int(input())
        b2 = int(input())
        a3 = int(input())
        b3 = int(input())
        a4 = int(input())
        b4 = int(input())
        gunnar_avg = (a1 + b1) / 2 + (a2 + b2) / 2
        emma_avg = (a3 + b3) / 2 + (a4 + b4) / 2
        if gunnar_avg > emma_avg:
            answers.append("Gunnar")
        elif gunnar_avg < emma_avg:
            answers.append("Emma")
        else:
            answers.append("Tie")
    print(*answers, sep="\n")