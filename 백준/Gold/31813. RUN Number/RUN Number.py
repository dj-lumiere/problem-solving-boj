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
    for hh in range(t):
        n = int(input())
        k = int(input())
        run_numbers = []
        for i in range(1, 10):
            run_numbers.extend([int(f"{i}" * j) for j in range(1, n + 1)])
        run_numbers.sort(reverse=True)
        answer = []
        for i in range(n + 1):
            if k == 0:
                break
            for v in run_numbers:
                if k >= v:
                    answer.append(v)
                    k -= v
                    break
        answer = f"{len(answer)}\n" + " ".join(map(str, answer))
        answers[hh] = f"{answer}"
    print(answers)