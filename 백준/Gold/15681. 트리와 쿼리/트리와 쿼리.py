from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
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


def dfs(root, graph, size):
    time = 0
    stack: list[tuple[int, bool]] = [(root, False)]
    time_in = [0] * (size + 1)
    time_out = [0] * (size + 1)
    while stack:
        node, visited = stack.pop()
        if not visited:
            time += 1
            time_in[node] = time
            stack.append((node, True))
            for child in reversed(graph[node]):
                if time_in[child] == 0:
                    stack.append((child, False))
        else:
            time_out[node] = time
    return time_in, time_out


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        r = int(input())
        q = int(input())
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            i, v = int(input()), int(input())
            graph[v].append(i)
            graph[i].append(v)
        time_in, time_out = dfs(root=r, graph=graph, size=n)
        for _ in range(q):
            u = int(input())
            answer = time_out[u] - time_in[u] + 1
            answers.append(f"{answer}")
    print(answers)