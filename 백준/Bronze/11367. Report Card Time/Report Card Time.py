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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())


        def convert_grade(grade):
            if 97 <= grade <= 100:
                return "A+"
            elif 90 <= grade <= 96:
                return "A"
            elif 87 <= grade <= 89:
                return "B+"
            elif 80 <= grade <= 86:
                return "B"
            elif 77 <= grade <= 79:
                return "C+"
            elif 70 <= grade <= 76:
                return "C"
            elif 67 <= grade <= 69:
                return "D+"
            elif 60 <= grade <= 66:
                return "D"
            else:
                return "F"


        results = []
        for _ in range(n):
            name = input()
            grade = int(input())
            letter_grade = convert_grade(grade)
            results.append(f"{name} {letter_grade}")
        answers.extend(results)
    print(*answers, sep="\n")