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
        X = int(input())
        N = int(input())
        threshold = Decimal(X) * Decimal(0.05)
        staff_votes = []
        for _ in range(N):
            name = input()
            votes = int(input())
            if votes >= threshold:
                staff_votes.append((name, votes))
        scores = []
        for name, votes in staff_votes:
            for i in range(1, 15):
                scores.append((Decimal(votes) / Decimal(i), name))
        scores.sort(reverse=True, key=lambda x: x[0])
        chips = {name: 0 for name, votes in staff_votes}
        for i in range(min(14, len(scores))):
            chips[scores[i][1]] += 1
        for name in sorted(chips):
            answers.append(f"{name} {chips[name]}")
    print(*answers, sep="\n")
