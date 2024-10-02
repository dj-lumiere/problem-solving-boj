from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt

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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        n, w = int(input()), int(input())
        samples = [int(input()) for _ in range(n)]
        moving_averages = []
        for i in range(n - w + 1):
            window_sum = sum(samples[i:i + w])
            moving_averages.append(window_sum // w)
        max_avg = max(moving_averages)
        min_avg = min(moving_averages)
        diff = abs(max_avg - min_avg)
        answers.append(f"Data Set {hh}:\n{diff}\n")
    print(*answers, sep="\n")
