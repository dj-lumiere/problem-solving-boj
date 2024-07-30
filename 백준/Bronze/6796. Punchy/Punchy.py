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
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 11092019
    answer = {"A": 0, "B": 0}
    for h in range(t):
        pass
    while True:
        q = int(input())
        if q == 7:
            break
        variable = input().decode()
        operand = 0
        if q in [1, 3, 4, 5, 6]:
            operand = input().decode()
        match q:
            case 1:
                answer[variable] = int(operand)
            case 2:
                answers.append(f"{answer[variable]}")
            case 3:
                answer[variable] += answer[operand]
            case 4:
                answer[variable] *= answer[operand]
            case 5:
                answer[variable] -= answer[operand]
            case 6:
                tmp = abs(answer[variable]) // abs(answer[operand])
                if (answer[variable] < 0) ^ (answer[operand] < 0):
                    tmp *= -1
                answer[variable] = tmp
    print(answers)