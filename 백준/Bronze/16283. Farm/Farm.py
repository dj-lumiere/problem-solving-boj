from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        a, b, n, w = [int(input()) for _ in range(4)]
        found_answer = False
        duplicate_answer = False
        answer = [0, 0]
        for i in range(1, n):
            j = n - i
            if a * i + b * j == w:
                if not found_answer:
                    found_answer = True
                    answer = [i, j]
                else:
                    duplicate_answer = True
                    break
        answer = -1 if duplicate_answer or not found_answer else f"{answer[0]} {answer[1]}"
        answers[h] = f"{answer}"
    print(answers)