from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from inspect import stack
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = 1
    answers = []
    for hh in range(1, x + 1):
        def merge(A, p, q, r, change_count):
            i = p
            j = q + 1
            t = 0
            tmp = [0] * (r - p + 1)

            while i <= q and j <= r:
                if A[i] <= A[j]:
                    tmp[t] = A[i]
                    i += 1
                else:
                    tmp[t] = A[j]
                    j += 1
                t += 1

            while i <= q:
                tmp[t] = A[i]
                i += 1
                t += 1

            while j <= r:
                tmp[t] = A[j]
                j += 1
                t += 1
            for t, val in enumerate(tmp):
                A[p + t] = val
                change_count[0] += 1
                if change_count[0] == K:
                    answers.extend(A)
                    return True
            return False


        def merge_sort(A, p, r, change_count):
            if p < r:
                q = (p + r) // 2
                if merge_sort(A, p, q, change_count):
                    return True
                if merge_sort(A, q + 1, r, change_count):
                    return True
                if merge(A, p, q, r, change_count):
                    return True
            return False


        N, K = int(input()), int(input())
        A = [int(input()) for _ in range(N)]
        change_count = [0]

        if not merge_sort(A, 0, N - 1, change_count):
            answers.append(-1)
    print(*answers, sep="\n")