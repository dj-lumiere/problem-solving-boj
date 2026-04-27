from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        r, c = int(input()), int(input())
        grid = [list(input().decode()) for _ in range(r)]
        start = [(y, x) for y, x in product(range(r), range(c)) if grid[y][x] == "S"]
        goals = [(y, x) for y, x in product(range(r), range(c)) if grid[y][x] == "G"]
        distance = [[INF for _ in range(c)] for _ in range(r)]
        queue = deque(start)
        for y, x in start:
            distance[y][x] = 0
        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = cur_r + dr
                new_c = cur_c + dc
                if not (0 <= new_r < r and 0 <= new_c < c):
                    continue
                if grid[new_r][new_c] == "X":
                    continue
                if distance[new_r][new_c] != INF:
                    continue
                distance[new_r][new_c] = distance[cur_r][cur_c] + 1
                queue.append((new_r, new_c))
        goal_distances = [distance[y][x] for y, x in goals]
        answer = "No Exit" if all(i == INF for i in goal_distances) else f"Shortest Path: {min(goal_distances)}"
        answers.append(f"{answer}")
    print(answers)