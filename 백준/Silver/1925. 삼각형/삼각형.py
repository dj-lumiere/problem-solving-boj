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
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 998244353
    for hh in range(t):
        x1, y1 = int(input()), int(input())
        x2, y2 = int(input()), int(input())
        x3, y3 = int(input()), int(input())
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
        b = ((x3 - x2) ** 2 + (y3 - y2) ** 2)
        c = ((x1 - x3) ** 2 + (y1 - y3) ** 2)
        a, b, c = sorted([a, b, c])
        answer = "X"
        if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
            if a == b == c:
                answer = "JungTriangle"
            else:
                t1, t2, t3 = a + b - c, b + c - a, c + a - b
                answer = ""
                if any(i < 0 for i in (t1, t2, t3)):
                    answer += "Dunkak"
                elif a + b == c:
                    answer += "Jikkak"
                else:
                    answer += "Yeahkak"
                if a == b or b == c or c == a:
                    answer += "2"
                answer += "Triangle"
        answers[hh] = answer
    print(answers)