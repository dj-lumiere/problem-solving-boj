from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
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
        l1, l2 = int(input()), int(input())
        s1 = bytes([100 + int(input()) for _ in range(l1)])
        s2 = bytes([100 + int(input()) for _ in range(l2)])
        eprint(s1, s2)
        answer = 0
        for i, j in combinations(range(l1 + 1), r=2):
            s1_sub = s1[i:j]
            if s1_sub in s2:
                answer = max(answer, len(s1_sub))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
