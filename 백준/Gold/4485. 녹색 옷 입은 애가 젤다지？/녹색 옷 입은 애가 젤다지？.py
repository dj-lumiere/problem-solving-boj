from collections import deque, Counter
from heapq import heappop, heappush
from itertools import product, chain
from sys import stdout, stderr
from time import perf_counter

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
    t = INF
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        if n == 0:
            break
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        minimum_rupee_loss = [[INF for _ in range(n)] for _ in range(n)]
        minimum_rupee_loss[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        while pq:
            rupee_loss, x, y = heappop(pq)
            if minimum_rupee_loss[y][x] < rupee_loss:
                continue
            for dx, dy in DELTA:
                if not is_inbound(x + dx, n, y + dy, n):
                    continue
                next_rupee_loss = rupee_loss + grid[y + dy][x + dx]
                if next_rupee_loss < minimum_rupee_loss[y + dy][x + dx]:
                    minimum_rupee_loss[y + dy][x + dx] = next_rupee_loss
                    heappush(pq, (next_rupee_loss, x + dx, y + dy))
        answer = minimum_rupee_loss[-1][-1]
        answers.append(f"Problem {hh}: {answer}")
    print(*answers, sep="\n")
