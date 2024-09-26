from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 30

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
        n = int(input())
        word = " " + input()
        visited = [False for _ in range(n + 1)]
        depth = [-1 for _ in range(n + 1)]
        tree = [[] for _ in range(n + 1)]
        parent = [-1 for _ in range(n + 1)]
        for _ in range(n - 1):
            a, b = int(input()), int(input())
            tree[a].append(b)
            tree[b].append(a)
        depth[1] = 0
        queue = deque()
        queue.append(1)
        visited[1] = True
        answer = [" " for _ in range(n)]
        answer[0] = word[1]
        while queue:
            current_node = queue.popleft()
            if depth[current_node] > 0 and word[parent[current_node]] != answer[depth[current_node] - 1]:
                answer[depth[current_node]] = " "
                continue
            if word[current_node] < answer[depth[current_node]]:
                continue
            answer[depth[current_node]] = word[current_node]
            for next_node in tree[current_node]:
                parent[next_node] = current_node
                if visited[next_node]:
                    continue
                visited[next_node] = True
                depth[next_node] = depth[current_node] + 1
                queue.append(next_node)
        answers.append(f"{''.join(answer).strip()}")
    print(*answers, sep="\n")
