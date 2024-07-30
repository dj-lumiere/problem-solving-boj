from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000


def is_inbound(pos_x, pos_y, size_x, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens) if tokens else ""
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for hh in range(t):
        n, m, k = [int(input()) for _ in range(3)]
        food = [[5 for _ in range(n)] for _ in range(n)]
        delta_food = [[int(input()) for _ in range(n)] for _ in range(n)]
        trees = [[dict() for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            y, x, z = [int(input()) for _ in range(3)]
            x -= 1
            y -= 1
            trees[y][x][z] = 1
        for a in range(1, k + 1):
            # Spring & Summer
            for r, c in product(range(n), repeat=2):
                trees_to_be_grown = dict()
                dead_tree_age_sum = 0
                if not trees[r][c]:
                    continue
                food_before = food[r][c]
                for i in range(1, max(trees[r][c].keys()) + 1):
                    if i not in trees[r][c]:
                        continue
                    current_trees = trees[r][c][i]
                    can_be_fed = min(food[r][c] // i, current_trees)
                    if can_be_fed < current_trees:
                        dead_tree_age_sum += (i // 2) * (current_trees - can_be_fed)
                    if can_be_fed:
                        trees_to_be_grown[i + 1] = can_be_fed
                        food[r][c] -= i * can_be_fed
                trees[r][c] = trees_to_be_grown
                food[r][c] += dead_tree_age_sum
            # Fall
            trees_to_be_grown = [[0 for _ in range(n)] for _ in range(n)]
            for r, c in product(range(n), repeat=2):
                for i in trees[r][c]:
                    if i % 5 != 0:
                        continue
                    for dr, dc in DELTA:
                        nr, nc = r + dr, c + dc
                        if not is_inbound(nc, nr, n, n):
                            continue
                        trees_to_be_grown[nr][nc] += trees[r][c][i]
            for r, c in product(range(n), repeat=2):
                sapling_count = trees[r][c].get(1, 0) + trees_to_be_grown[r][c]
                if sapling_count:
                    trees[r][c][1] = sapling_count
            # Winter
            for r, c in product(range(n), repeat=2):
                food[r][c] += delta_food[r][c]
        answer = sum(sum(trees[r][c].values()) for r, c in product(range(n), repeat=2))
        answers.append(f"{answer}")
    print(*answers, sep="\n")