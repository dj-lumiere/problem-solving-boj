from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from inspect import stack
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        R = int(input())
        C = int(input())
        pasture = []
        for i in range(R):
            pasture.append(input())
        visited = []
        for i in range(R):
            visited.append([False] * C)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, col):
            stack = [(row, col)]
            visited[row][col] = True
            while len(stack) > 0:
                current_row, current_col = stack.pop()
                for direction in directions:
                    new_row = current_row + direction[0]
                    new_col = current_col + direction[1]
                    if 0 <= new_row < R and 0 <= new_col < C:
                        if pasture[new_row][new_col] == '#' and not visited[new_row][new_col]:
                            visited[new_row][new_col] = True
                            stack.append((new_row, new_col))
        grass_clumps = 0
        for i in range(R):
            for j in range(C):
                if pasture[i][j] == '#' and not visited[i][j]:
                    dfs(i, j)
                    grass_clumps += 1
        answers.append(grass_clumps)
    print(*answers, sep="\n")