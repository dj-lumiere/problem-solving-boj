from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        w, h, k = int(input()), int(input()), int(input())
        # 마름모용 그리드 (상하좌우로 두 칸씩 패딩 필요)
        grid_rhombus = [[0 for c in range(w + 4)] for r in range(h + 4)]
        # 직사각형용 그리드 (상하좌우로 두 칸씩 동일하게 패딩)
        grid_rectangle = [[0 for _ in range(w + 4)] for _ in range(h + 4)]
        # imos법 사용
        # 마름모는 8칸만 기록하고 우하향, 좌하향, 좌우 순으로 누적합
        # 직사각형은 4칸만 기록하고 상하, 좌우 순으로 누적합
        for _ in range(k):
            shape = int(input())
            if shape == 1:
                px, py, qx, qy = (int(input()) + 2 for _ in range(4))
                grid_rectangle[py][px] += 1
                grid_rectangle[qy + 1][qx + 1] += 1
                grid_rectangle[qy + 1][px] -= 1
                grid_rectangle[py][qx + 1] -= 1
            elif shape == 2:
                px, py, r = (int(input()) + 2 for _ in range(3))
                r -= 2
                grid_rhombus[py - r][px] += 1
                grid_rhombus[py - r + 1][px] += 1
                grid_rhombus[py + r + 1][px] += 1
                grid_rhombus[py + r + 2][px] += 1
                grid_rhombus[py + 1][px - r + 1] += 1
                grid_rhombus[py + 1][px + r + 2] += 1
                grid_rhombus[py - r][px + 1] -= 1
                grid_rhombus[py - r + 1][px + 1] -= 1
                grid_rhombus[py + r + 1][px + 1] -= 1
                grid_rhombus[py + r + 2][px + 1] -= 1
                grid_rhombus[py + 1][px - r - 1] -= 1
                grid_rhombus[py + 1][px + r] -= 1
        # 우하향
        for r, dy_minus_dx in enumerate(range(-w - 3, h + 4)):
            if dy_minus_dx < 0:
                x, y = -dy_minus_dx, 0
            else:
                x, y = 0, dy_minus_dx
            x += 1
            y += 1
            while is_inbound(x, w + 4, y, h + 4):
                grid_rhombus[y][x] += grid_rhombus[y - 1][x - 1]
                x += 1
                y += 1
        # 좌하향
        for r, dy_plus_dx in enumerate(range(w + h + 8)):
            if dy_plus_dx >= w + 4:
                x, y = w + 3, dy_plus_dx - w - 3
            else:
                x, y = dy_plus_dx, 0
            x -= 1
            y += 1
            while is_inbound(x, w + 4, y, h + 4):
                grid_rhombus[y][x] += grid_rhombus[y - 1][x + 1]
                x -= 1
                y += 1
        # 좌우
        for y in range(h + 4):
            x = 1
            while is_inbound(x, w + 4, y, h + 4):
                grid_rhombus[y][x] += grid_rhombus[y][x - 1]
                x += 1
        # 상하
        for x in range(w + 4):
            y = 1
            while is_inbound(x, w + 4, y, h + 4):
                grid_rectangle[y][x] += grid_rectangle[y - 1][x]
                y += 1
        # 좌우
        for y in range(h + 4):
            x = 1
            while is_inbound(x, w + 4, y, h + 4):
                grid_rectangle[y][x] += grid_rectangle[y][x - 1]
                x += 1
        grid_total = [["." for _ in range(w)] for _ in range(h)]
        for x, y in product(range(w), range(h)):
            if (grid_rectangle[y + 2][x + 2] + grid_rhombus[y + 2][x + 2]) & 1:
                grid_total[y][x] = "#"
        answer = "\n".join("".join(v) for v in grid_total)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
