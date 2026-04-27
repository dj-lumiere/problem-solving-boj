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
        n = int(input())
        z = int(input())
        m = int(input())
        available = [0 for _ in range(n)]
        for i in range(m):
            available[int(input()) - 1] = -1
        answer = 0
        available[0] = 1
        for k in range(1, n + 1):
            found_answer = False
            for i in range(0, k * n, k):
                if available[i % n] == -1:
                    break
                if i % n == z - 1:
                    found_answer = True
                    break
                available[i % n] = 1
            if found_answer:
                answer = k
                break
        answers[h] = f"{answer}"
    print(answers)