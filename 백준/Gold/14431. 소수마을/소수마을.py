from collections import deque, Counter
from itertools import product, chain, permutations, combinations, repeat
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt
from heapq import heappush, heappop


def get_prime_sieve(limit: int) -> list[bool]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return is_prime


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
    is_prime = get_prime_sieve(12000)
    for hh in range(1, t + 1):
        x1, y1, x2, y2 = (int(input()) for _ in range(4))
        n = int(input())
        nodes = [(int(input()), int(input())) for _ in range(n)]
        lines = [[] for _ in range(n + 2)]
        max_line = -INF
        distance_sub = isqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if is_prime[distance_sub]:
            lines[0].append((n + 1, distance_sub))
            lines[n + 1].append((0, distance_sub))
        for i, (v1, v2) in enumerate(nodes, start=1):
            distance_sub1 = isqrt((x1 - v1) ** 2 + (y1 - v2) ** 2)
            distance_sub2 = isqrt((x2 - v1) ** 2 + (y2 - v2) ** 2)
            max_line = max(max_line, distance_sub1, distance_sub2)
            if is_prime[distance_sub1]:
                lines[0].append((i, distance_sub1))
                lines[i].append((0, distance_sub1))
            if is_prime[distance_sub2]:
                lines[n + 1].append((i, distance_sub2))
                lines[i].append((n + 1, distance_sub2))
        for (i, (v1, v2)), (j, (v3, v4)) in product(enumerate(nodes, start=1), repeat=2):
            if i <= j:
                continue
            distance_sub = isqrt((v1 - v3) ** 2 + (v2 - v4) ** 2)
            max_line = max(max_line, distance_sub)
            if is_prime[distance_sub]:
                lines[i].append((j, distance_sub))
                lines[j].append((i, distance_sub))
        queue = [(0, 0)]  # (distance, node)
        cost_list = [INF for _ in range(n + 2)]
        while queue:
            cur_dist, cur_node = heappop(queue)
            if cost_list[cur_node] < cur_dist:
                continue
            for i, j in lines[cur_node]:
                next_cost = cur_dist + j
                if next_cost < cost_list[i]:
                    cost_list[i] = next_cost
                    heappush(queue, (next_cost, i))
        answer = -1 if cost_list[n + 1] == INF else cost_list[n + 1]
        answers.append(answer)
    print(*answers, sep="\n")
