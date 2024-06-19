from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    arrangement = {'`': 0, '1': 0, '2': 1, '3': 2, '4': 3, '5': 3, '6': 4, '7': 4, '8': 5, '9': 6, '0': 7, '-': 7, '=': 7, 'Q': 0, 'W': 1, 'E': 2, 'R': 3, 'T': 3, 'Y': 4, 'U': 4, 'I': 5, 'O': 6, 'P': 7, '[': 7, ']': 7, 'A': 0, 'S': 1, 'D': 2, 'F': 3, 'G': 3, 'H': 4, 'J': 4, 'K': 5, 'L': 6, ';': 7, "'": 7, 'Z': 0, 'X': 1, 'C': 2, 'V': 3, 'B': 3, 'N': 4, 'M': 4, ',': 5, '.': 6, '/': 7}
    for hh in range(t):
        x = input().decode()
        y = [0 for _ in range(8)]
        for i in x:
            y[arrangement[i]] += 1
        answer = "\n".join(map(str, y))
        answers.append(f"{answer}")
    print(answers)