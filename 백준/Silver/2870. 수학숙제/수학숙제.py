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
        n = int(input())
        numbers = []
        for _ in range(n):
            x = input().decode()
            tmp = 0
            number_digit = 0
            for i, v in enumerate(x):
                if ord('0') <= ord(v) <= ord('9'):
                    tmp *= 10
                    tmp += int(v)
                    number_digit += 1
                elif number_digit:
                    numbers.append(tmp)
                    tmp = 0
                    number_digit = 0
            else:
                if number_digit:
                    numbers.append(tmp)
                    tmp = 0
                    number_digit = 0
        numbers = sorted(numbers)
        answer = "\n".join(map(str, numbers))
        answers[h] = f"{answer}"
    print(answers)