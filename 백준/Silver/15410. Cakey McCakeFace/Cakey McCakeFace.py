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
        M = int(input())
        entry_times = [int(input()) for _ in range(N)]
        exit_times = [int(input()) for _ in range(M)]
        time_differences = Counter()
        for exit_time in exit_times:
            for entry_time in entry_times:
                if exit_time >= entry_time:
                    cooking_time = exit_time - entry_time
                    if cooking_time not in time_differences:
                        time_differences[cooking_time] = 0
                    time_differences[cooking_time] += 1
        max_frequency = max(*time_differences.values()) if time_differences else 0
        best_cooking_time = min(k for k, v in time_differences.items() if v == max_frequency) if time_differences else 0
        answers.append(best_cooking_time)
    print(*answers, sep="\n")
