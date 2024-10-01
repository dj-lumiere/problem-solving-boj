from bisect import bisect_left, bisect_right
from collections import Counter, deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from operator import index
from sys import stdout, stderr
from itertools import permutations, product

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        r, c, h, w = (int(input()) for _ in range(4))
        grid = [[int(input()) for _ in range(c)] for _ in range(r)]
        answer = 0
        start = 0
        end = r * c
        while start + 1 < end:
            mid = (start + end) // 2
            is_bigger = [[0 if grid[y][x] == mid else (grid[y][x] - mid) // abs(grid[y][x] - mid) for x in range(c)] for
                         y in range(r)]
            accumulated_sum = [[0] * (c + 1)] + [[0] + [is_bigger[y][x] for x in range(c)] for y in range(r)]
            for x, y in product(range(1, c), range(r)):
                accumulated_sum[y + 1][x + 1] += accumulated_sum[y + 1][x]
            for x, y in product(range(c), range(1, r)):
                accumulated_sum[y + 1][x + 1] += accumulated_sum[y][x + 1]
            for x, y in product(range(c - w + 1), range(r - h + 1)):
                bigger_than_mid_count = accumulated_sum[y + h][x + w] - accumulated_sum[y + h][x] - \
                                        accumulated_sum[y][x + w] + accumulated_sum[y][x]
                if bigger_than_mid_count <= 0:
                    end = mid
                    break
            else:
                start = mid
        answer = end
        answers.append(f"{answer}")
    print(*answers, sep="\n")