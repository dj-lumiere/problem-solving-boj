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
    while True:
        number = input().decode()
        if number == "0":
            break
        number += " "
        answer = ""
        current = ""
        count = 0
        for i, v in enumerate(number):
            if i == 0:
                current = v
                count = 1
                continue
            if v != current:
                answer += f"{count}{current}"
                current = v
                count = 1
            else:
                count += 1
        answers.append(answer)
    print(answers)