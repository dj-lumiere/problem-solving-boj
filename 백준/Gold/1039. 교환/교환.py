from bisect import bisect_left, bisect_right
from collections import deque
from decimal import Decimal
from heapq import heappop, heappush
from itertools import product, combinations
from math import ceil, log2, atan2, pi, sqrt, cos, sin, gcd, lcm
from array import array
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        n, k = int(input()), int(input())
        max_number = -INF
        if 0 <= n <= 9:
            answer = -1
        else:
            visited = [array("b", [0 for _ in range(10 ** len(str(n)))]) for _ in range(k + 1)]
            visited[0][n] = 1
            queue = deque([(0, n)])
            while queue:
                count, current = queue.popleft()
                if count == k:
                    continue
                for i, j in combinations(range(len(str(current))), r=2):
                    next_string = list(map(int, str(current)))
                    next_string[i], next_string[j] = next_string[j], next_string[i]
                    if next_string[0] == 0:
                        continue
                    next_number = int("".join(map(str, next_string)))
                    if visited[count + 1][next_number]:
                        continue
                    visited[count + 1][next_number] = 1
                    queue.append((count + 1, next_number))
            answer = max(i for i, v in enumerate(visited[-1]) if v) if any(visited[-1]) else -1
        answers.append(f"{answer}")
    print(*answers, sep="\n")
