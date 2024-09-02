from collections import deque, Counter
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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        size = 101
        sequence = [[[] for _ in range(11)] for _ in range(4)]
        for h in range(4):
            sequence[h][0] = [h]
            # 한 칸씩 밀고 방향 뒤집기
            for i in range(1, 11):
                sequence[h][i] = sequence[h][i - 1][:]
                for v in reversed(sequence[h][i - 1]):
                    sequence[h][i].append((v + 3) % 4)
        grid = [[0 for _ in range(101)] for _ in range(101)]
        curves = [[int(input()) for _ in range(4)] for _ in range(N)]
        for x, y, d, g in curves:
            if d == 1:
                d = 3
            elif d == 3:
                d = 1
            curve = sequence[d][g]
            grid[y][x] = 1
            for move in curve:
                dx, dy = DELTA[move]
                nx, ny = x + dx, y + dy
                if is_inbound(nx, size, ny, size):
                    grid[ny][nx] = 1
                x, y = nx, ny
        answer = sum(grid[y][x] == grid[y + 1][x] == grid[y][x + 1] == grid[y + 1][x + 1] == 1 for x, y in
                     product(range(100), repeat=2))
        answers.append(f"{answer}")
print(*answers, sep="\n")
