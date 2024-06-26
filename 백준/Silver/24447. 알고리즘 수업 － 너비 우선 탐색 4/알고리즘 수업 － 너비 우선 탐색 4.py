from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
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
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep="\n", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n, m, r = int(input()), int(input()), int(input())
        graph = [[] for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        order = [0 for _ in range(n + 1)]
        depth = [0 for _ in range(n + 1)]
        for _ in range(m):
            i, v = int(input()), int(input())
            graph[i].append(v)
            graph[v].append(i)
        graph = list(map(sorted, graph))
        visited[r] = True
        order[r] = 0
        depth[r] = 0
        queue = deque()
        queue.append(r)
        visited_count = 1
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    visited_count += 1
                    order[v] = visited_count
                    depth[v] = max(depth[v], depth[u] + 1)
                    queue.append(v)
        answer = sum(i * v for i, v in zip(depth[1:], order[1:]))
        answers.append(f"{answer}")
    print(*answers)