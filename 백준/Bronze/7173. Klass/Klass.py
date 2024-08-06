from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())


    def input():
        try:
            return next(tokens)
        except StopIteration:
            return ""


    print = lambda *args, sep="\n", end="\n": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for hh in range(t):
        M = int(input())
        N = int(input())
        grid = [list(map(int, input())) for _ in range(M)]
        total_distraction = 0.0

        for y in range(M):
            for x in range(N):
                interest = grid[y][x]
                neighbor_count = 0
                total_difference = 0

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_inbound(nx, N, ny, M):
                        neighbor_interest = grid[ny][nx]
                        total_difference += abs(interest - neighbor_interest)
                        neighbor_count += 1

                if neighbor_count > 0:
                    average_difference = total_difference / neighbor_count
                    total_distraction += average_difference
        answer = f"{total_distraction:.4f}"
        answers.append(f"{answer}")
    print(*answers)