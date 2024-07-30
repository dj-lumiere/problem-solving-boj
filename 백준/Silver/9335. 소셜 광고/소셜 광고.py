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
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        connected = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            x = int(input())
            connected[i].extend(int(input()) for _ in range(x))
        answer = n
        for mask in range(1, 1 << n):
            is_visible = [True] + [False] * n
            for j in range(n):
                if mask & (1 << j) != 0:
                    is_visible[j + 1] = True
                    for k in connected[j + 1]:
                        is_visible[k] = True
            if all(is_visible):
                answer = min(answer, mask.bit_count())
        answers[h] = f"{answer}"
    print(answers)