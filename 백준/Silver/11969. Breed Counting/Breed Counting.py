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
        q = int(input())
        answer = ["" for _ in range(q)]
        cows = [int(input()) for _ in range(n)]
        cow_quantity = [[int(i == j) for i in cows] for j in range(1, 3 + 1)]
        cow_quantity_accsum = [[0] for _ in range(3)]
        for i, v in enumerate(cow_quantity):
            for j, v2 in enumerate(v):
                cow_quantity_accsum[i].append(v2 + cow_quantity_accsum[i][-1])
        for i in range(q):
            a, b = int(input()), int(input())
            answer_sub = [cow_quantity_accsum[i][b] - cow_quantity_accsum[i][a - 1] for i in range(3)]
            answer[i] = " ".join(map(str, answer_sub))
        answers[h] = "\n".join(answer)
    print(answers)