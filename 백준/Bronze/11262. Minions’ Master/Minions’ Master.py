from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
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
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        a_sum = sum(a)
        over_average = sum(i * n > a_sum for i in a)
        answer1 = sum(a) * 10000 // n
        answer2 = over_average * 100 * 10000 // n
        if answer1 % 10 >= 5:
            answer1 //= 10
            answer1 += 1
        else:
            answer1 //= 10
        if answer2 % 10 >= 5:
            answer2 //= 10
            answer2 += 1
        else:
            answer2 //= 10
        answers[h] = f"{answer1/1000:.3f} {answer2/1000:.3f}%"
    print(answers)