from collections import deque, Counter
from itertools import product, chain, permutations, combinations, repeat
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt
from heapq import heappush, heappop

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        cows = []
        for _ in range(N):
            s = int(input())
            t = int(input())
            b = int(input())
            cows.append((s, t, b))
        bucket_usage = [0] * 1001
        for cow in cows:
            start, end, buckets_needed = cow
            for time in range(start, end):
                bucket_usage[time] += buckets_needed
        max_buckets = 0
        for i in range(1001):
            if bucket_usage[i] > max_buckets:
                max_buckets = bucket_usage[i]
        answers.append(max_buckets)
    print(*answers, sep="\n")
