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
    T = 1
    answers = []
    dp = [[0 for _ in range(10 ** i + 1)] for i in range(1, 7)] + [[0 for _ in range(10 ** 7 + 1)]]
    for hh in range(1, T + 1):
        n = input()
        # bitmasking (0 means stick to left, 1 means stick to right)
        paths = set()
        for mask in range(1 << (len(n) - 1)):
            stick_direction = [mask & (1 << i) != 0 for i in range(len(n) - 1)]
            first_digit_index = len(n) - 1 - sum(stick_direction)
            right_sticks = 0
            left_sticks = 0
            path = [n[first_digit_index]]
            for i, v in enumerate(stick_direction):
                if v:
                    right_sticks += 1
                    path.append(path[-1] + n[first_digit_index + right_sticks])
                else:
                    left_sticks += 1
                    path.append(n[first_digit_index - left_sticks] + path[-1])
            paths.add(tuple(map(int, path)))
        result = len(paths)
        answers.append(result)
    print(*answers, sep="\n")
