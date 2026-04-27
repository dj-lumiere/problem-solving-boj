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

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        m = int(input())
        graph = [[] for _ in range(n + 1)]
        distance = [0 for _ in range(n + 1)]
        for _ in range(m):
            a, b = int(input()), int(input())
            graph[a].append(b)
            graph[b].append(a)
        distance[1] = 1
        queue = deque()
        queue.append(1)
        while queue:
            current_node = queue.popleft()
            for next_node in graph[current_node]:
                if distance[next_node] != 0:
                    continue
                distance[next_node] = distance[current_node] + 1
                queue.append(next_node)
        answer = sum(2 <= v <= 3 for v in distance)
        answers.append(f"{answer}")
    print(answers)