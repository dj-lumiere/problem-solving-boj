from bisect import bisect_left
from string import ascii_lowercase
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
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        r = int(input())
        c = int(input())
        grid = [list(map(int, input().decode())) for _ in range(r)]
        q = int(input())
        answer = [f"Case #{h + 1}:"]
        for _ in range(q):
            opcode = input().decode()
            if opcode == "M":
                y, x, z = [int(input()) for _ in range(3)]
                grid[y][x] = z
            if opcode == "Q":
                visited = [[False for _ in range(c)] for _ in range(r)]
                island_count = 0
                DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for y in range(r):
                    for x in range(c):
                        if visited[y][x]:
                            continue
                        if grid[y][x] == 0:
                            continue
                        island_count += 1
                        visit_queue = deque([(x, y)])
                        visited[y][x] = True
                        while visit_queue:
                            cur_x, cur_y = visit_queue.pop()
                            for dx, dy in DELTA:
                                next_x, next_y = cur_x + dx, cur_y + dy
                                if not (0 <= next_x < c and 0 <= next_y < r):
                                    continue
                                if grid[next_y][next_x] == 0:
                                    continue
                                if visited[next_y][next_x]:
                                    continue
                                visited[next_y][next_x] = True
                                visit_queue.append((next_x, next_y))
                answer.append(island_count)
        answers[h] = "\n".join(map(str, answer))
    print(answers)