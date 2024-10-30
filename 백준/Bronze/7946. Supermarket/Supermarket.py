from bisect import bisect_left, bisect_right
from decimal import Decimal
from heapq import heappop, heappush
from itertools import product, combinations
from math import ceil, log2, atan2, pi, sqrt, cos, sin, gcd, lcm
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for hh in range(t):
        n, k = int(input()), int(input())
        counts = [0] * 100001
        for _ in range(n):
            num = int(input())
            counts[num] += 1
        cumulative = 0
        for num in range(1, 100001):
            cumulative += counts[num]
            if cumulative >= k:
                answer = num
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")
