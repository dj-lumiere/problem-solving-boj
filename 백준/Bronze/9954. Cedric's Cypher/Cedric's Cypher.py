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
    tokens = iter(f.read().split(b"\n"))


    def input():
        try:
            return next(tokens)
        except StopIteration:
            return ""


    print = lambda *args, sep="\n", end="\n": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for hh in range(t):
        s = input().decode()
        if s == "#":
            break
        offset = ord(s[-1]) - ord("A")
        s = s[:-1]
        answer = ""
        for i, v in enumerate(s):
            if not v.isalpha():
                answer += v
                continue
            if v.islower():
                decoded = chr((ord(v) - ord("a") - offset) % 26 + ord("a"))
            else:
                decoded = chr((ord(v) - ord("A") - offset) % 26 + ord("A"))
            answer += decoded
        answers.append(f"{answer}")
    print(*answers)