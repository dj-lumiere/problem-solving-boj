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
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        pass
    base = [1]
    connection = [""]
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        base.append(base[-1] * i)
        connection.append(connection[-1] + "*" + str(i))
    while True:
        n = int(input())
        if not n:
            break
        n2 = n
        conversion = [0 for _ in range(len(base))]
        for i, v in enumerate(reversed(base)):
            conversion[i] += n2 // v
            n2 -= conversion[i] * v
        conversion.reverse()
        answer = [str(n), "="]
        for i, v in enumerate(conversion):
            if not v:
                continue
            answer.append(f"{v}{connection[i]}")
            answer.append("+")
        answer.pop()
        answers.append(" ".join(answer))
    print(answers)