from bisect import bisect_left, bisect_right
from collections import deque, Counter
from heapq import heappop, heappush
from itertools import product, chain, combinations
from string import ascii_lowercase
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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = 21
        grid = [[0 for _ in range(8)] for _ in range(7)]
        current_position = [0 for _ in range(8)]
        answer = "ss"
        connect_4 = lambda grid: any(
            (*(all(grid[r + x][c] == grid[r][c] != 0 for x in range(4)) for r, c in product(range(4), range(1, 8))),
             *(all(grid[r][c + x] == grid[r][c] != 0 for x in range(4)) for r, c in product(range(7), range(1, 5))),
             *(all(grid[r + x][c + x] == grid[r][c] != 0 for x in range(4)) for r, c in product(range(4), range(1, 5))),
             *(all(grid[r - x][c + x] == grid[r][c] != 0 for x in range(4)) for r, c in product(range(3, 7), range(1, 5)))),
        )
        for M in range(1, n + 1):
            si, ji = int(input()), int(input())
            grid[current_position[si]][si] = 1
            current_position[si] += 1
            if connect_4(grid):
                answer = f"sk {M}"
                break
            grid[current_position[ji]][ji] = 2
            current_position[ji] += 1
            if connect_4(grid):
                answer = f"ji {M}"
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")
