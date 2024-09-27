from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from heapq import heappush, heappop

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
    for hh in range(1, t + 1):
        n, m = int(input()), int(input())
        grid = [list(map(int, input())) for _ in range(m)]
        minimum_wall_to_destroy = [[INF for _ in range(n)] for _ in range(m)]
        minimum_wall_to_destroy[0][0] = 0
        queue = [(0, 0, 0)]
        while queue:
            ccost, cx, cy = heappop(queue)
            for dx, dy in DELTA:
                nx, ny = cx + dx, cy + dy
                if not is_inbound(nx, n, ny, m):
                    continue
                ncost = ccost + grid[ny][nx]
                if ncost >= minimum_wall_to_destroy[ny][nx]:
                    continue
                minimum_wall_to_destroy[ny][nx] = min(minimum_wall_to_destroy[ny][nx], ncost)
                heappush(queue, (ncost, nx, ny))
        answer = minimum_wall_to_destroy[-1][-1]
        answers.append(f"{answer}")
    print(*answers, sep="\n")
