from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        v = int(input())
        p = int(input())
        l = int(input())
        towns = [int(input()) for _ in range(v)]
        min_dist = 2 * p * 10 ** 18
        answer = ()
        for post in combinations(sorted(towns), p):
            answer_sub = 0
            for j in towns:
                answer_sub += min(min(abs(i - j), l - abs(i - j)) for i in post)
            if answer_sub < min_dist:
                min_dist = answer_sub
                answer = post
        answers[h] = f'{min_dist}\n' + ' '.join(map(str, answer))
    print(answers)