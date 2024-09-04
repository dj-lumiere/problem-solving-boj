from bisect import bisect_left, bisect_right
from collections import deque, Counter
from heapq import heappop, heappush
from itertools import product, chain, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter

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
        x, y = int(input()), int(input())
        answer = 0
        for i in range(16):
            if x & (1 << i) != 0:
                answer |= 1 << (2 * i + 1)
            if y & (1 << i) != 0:
                answer |= 1 << (2 * i)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
