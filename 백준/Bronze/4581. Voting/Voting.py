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


    def input():
        try:
            return next(tokens)
        except StopIteration:
            return ""


    print = lambda *args, sep="\n", end="\n": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    for hh in range(t):
        s = input().decode()
        if s == "#":
            break
        votes = Counter(s)
        for i in "YNPA":
            if i not in votes:
                votes[i] = 0
        if votes["A"] * 2 >= len(s):
            answer = "need quorum"
        elif votes["Y"] > votes["N"]:
            answer = "yes"
        elif votes["N"] > votes["Y"]:
            answer = "no"
        else:
            answer = "tie"
        answers.append(answer)
    print(*answers)