from bisect import bisect_left
from string import ascii_uppercase, ascii_lowercase
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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 10 ** 9
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        words = [input().decode() for _ in range(n)]
        answer = 0
        current = ""
        lengths = [0, 5,7,5,7,7]
        for i, v in enumerate(words, start=1):
            current = [v]
            for j, v2 in enumerate(words, start=1):
                if i >= j:
                    continue
                if len(current[-1]) + len(v2) > lengths[len(current)]:
                    current.append("")
                if len(current) >= 6:
                    current.pop()
                    break
                current[-1] += v2
            if all(len(v3) == lengths[k] for k, v3 in enumerate(current, start=1)):
                answer = i
                break
        answers.append(f"{answer}")
    print(answers)