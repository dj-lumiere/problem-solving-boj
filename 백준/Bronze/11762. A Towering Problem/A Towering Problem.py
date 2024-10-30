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
    t = 1
    answers = []
    for hh in range(t):
        boxes = [int(input()) for _ in range(6)]
        t1 = int(input())
        t2 = int(input())
        found = False
        for i, j, k in combinations(range(6), r=3):
            if boxes[i] + boxes[j] + boxes[k] == t1:
                tower1 = sorted([boxes[i], boxes[j], boxes[k]], reverse=True)
                remaining = [boxes[x] for x in range(6) if x not in [i, j, k]]
                tower2 = sorted(remaining, reverse=True)
                answer = ' '.join(map(str, tower1 + tower2))
                found = True
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")
