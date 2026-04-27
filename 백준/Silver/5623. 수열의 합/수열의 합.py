from time import perf_counter_ns, sleep
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


def to_time(x):
    h, m = x.split(":")
    return int(h) * 60 + int(m)


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        sums = [[int(input()) for _ in range(n)] for _ in range(n)]
        answer = [0 for _ in range(n)]
        if n == 2:
            if sums[1][0] & 1:
                answer[0] = sums[1][0] // 2
                answer[1] = sums[1][0] // 2 + 1
            else:
                answer[0] = sums[1][0] // 2
                answer[1] = sums[1][0] // 2
        else:
            answer[0] = (sums[0][1] + sums[0][2] - sums[2][1]) // 2
            for i in range(1, n):
                answer[i] = sums[i][0] - answer[0]
        answers[h] = " ".join(map(str, answer))
    print(answers)