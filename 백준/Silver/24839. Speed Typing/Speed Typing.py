from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from itertools import product
from math import ceil, log2, atan2, pi, sqrt, cos, sin
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
        I = input()
        P = input()
        i = 0
        for c in P:
            if i < len(I) and c == I[i]:
                i += 1
        if i == len(I):
            answer = len(P) - len(I)
        else:
            answer = "IMPOSSIBLE"
        answers.append(f"Case #{hh + 1}: {answer}")
    print(*answers, sep="\n")
