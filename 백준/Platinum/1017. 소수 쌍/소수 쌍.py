"""from https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/hopcroft_karp.py"""

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


def hopcroft_karp(graph, n, m):
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


def get_prime_sieve(limit: int) -> list[bool]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return is_prime


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
        n = int(input())
        numbers = [int(input()) for _ in range(n)]
        result = []
        is_prime = get_prime_sieve(2001)
        first_match = [i for i, v in enumerate(numbers) if i != 0 and is_prime[v + numbers[0]]]
        for i in first_match:
            graph = [[] for _ in range(n)]
            for (i1, n1), (i2, n2) in combinations(enumerate(numbers), 2):
                if is_prime[n1 + n2] and i1 != 0 and i2 != 0 and i1 != i and i2 != i:
                    graph[i1].append(i2)
                    graph[i2].append(i1)
            _, match = hopcroft_karp(graph, n, n)
            match[0] = i
            match[i] = 0
            if match.count(-1) == 0:
                result.append(numbers[i])
        answer = " ".join(map(str, sorted(result))) if result else "-1"
        answers.append(f"{answer}")
    print(*answers)