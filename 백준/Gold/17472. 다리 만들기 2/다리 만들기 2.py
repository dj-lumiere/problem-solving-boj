from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

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
    for hh in range(t):
        n, m = int(input()), int(input())
        grid = [[int(input()) for _ in range(m)] for _ in range(n)]
        island_grid = [[0 for _ in range(m)] for _ in range(n)]
        island_count = 1
        for r, c in product(range(n), range(m)):
            if grid[r][c] == 0:
                continue
            queue = deque([(r, c)])
            island_grid[r][c] = island_count
            while queue:
                y, x = queue.popleft()
                for dx, dy in DELTA:
                    nx, ny = x + dx, y + dy
                    if not is_inbound(nx, m, ny, n):
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    grid[ny][nx] = 0
                    island_grid[ny][nx] = island_count
                    queue.append((ny, nx))
            island_count += 1
        #eprint(*island_grid, sep="\n")
        #eprint(island_count)
        possible_bridges = []
        for i, j in combinations(range(1, island_count), r=2):
            #eprint(i, j)
            distance = INF
            distance_sub = INF
            for (r1, c1), (r2, c2) in product(product(range(n), range(m)), repeat=2):
                if not (island_grid[r1][c1] == i and island_grid[r2][c2] == j):
                    continue
                if r1 == r2 and all(island_grid[r1][c] == 0 for c in range(min(c1, c2)+1, max(c1, c2))):
                    distance_sub = abs(c1 - c2) - 1
                    if distance_sub == 1:
                        continue
                    distance = min(distance, distance_sub)
                    #eprint(r1, c1, r2, c2, distance_sub)
                if c1 == c2 and all(island_grid[r][c1] == 0 for r in range(min(r1, r2)+1, max(r1, r2))):
                    distance_sub = abs(r1 - r2) - 1
                    if distance_sub == 1:
                        continue
                    distance = min(distance, distance_sub)
                    #eprint(r1, c1, r2, c2, distance_sub)
            if distance == INF:
                continue
            possible_bridges += [(i, j, distance)]
        #eprint(possible_bridges)
        total_cost = INF
        for bridges in combinations(possible_bridges, r=island_count - 2):
            #eprint(bridges)
            is_approachable = [False] * island_count
            graph = [[] for _ in range(island_count)]
            for i, j, _ in bridges:
                graph[i].append(j)
                graph[j].append(i)
            stack = [1]
            is_approachable[0] = is_approachable[1] = True
            while stack:
                cur = stack.pop()
                for i in graph[cur]:
                    if is_approachable[i]:
                        continue
                    is_approachable[i] = True
                    stack.append(i)
            #eprint(is_approachable)
            if not all(is_approachable):
                continue
            current_cost = sum(distance for _, _, distance in bridges)
            #eprint(current_cost)
            total_cost = min(total_cost, current_cost)
        answer = total_cost if total_cost != INF else -1
        answers.append(f"{answer}")
    print(*answers, sep="\n")
