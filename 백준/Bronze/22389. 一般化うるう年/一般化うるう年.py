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
    t = INF
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        if n == 0:
            break
        l, r = int(input()), int(input())
        A = [int(input()) for _ in range(n)]


        def is_generalized_leap_year(x):
            for i, v in enumerate(A, start=1):
                if x % v == 0:
                    return i % 2 == 1
            return n % 2 == 0


        count = sum(1 for x in range(l, r + 1) if is_generalized_leap_year(x))
        answers.append(count)
    print(*answers, sep="\n")
