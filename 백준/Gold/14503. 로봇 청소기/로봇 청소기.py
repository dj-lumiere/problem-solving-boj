from collections import deque
from itertools import product
from sys import stdout, stderr

from __pypy__ import newlist_hint

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    CLEANED = 2
    NOT_CLEANED = 0
    WALL = 1
    t = 1
    answers = newlist_hint(t)
    for hh in range(t):
        n, m = int(input()), int(input())
        r, c, d = (int(input()) for _ in range(3))
        grid = [[int(input()) for _ in range(m)] for _ in range(n)]
        queue = deque([(c, r)])
        while queue:
            x, y = queue.popleft()
            if grid[y][x] == NOT_CLEANED:
                grid[y][x] = CLEANED
            if all(grid[y + dy][x + dx] in (CLEANED, WALL) for dx, dy in DELTA):
                dx, dy = DELTA[d]
                nx, ny = x - dx, y - dy
                if grid[ny][nx] == WALL:
                    break
                queue.append((nx, ny))
            else:
                for i in reversed(range(d, d + 4)):
                    dx, dy = DELTA[i % 4]
                    nx, ny = x + dx, y + dy
                    if grid[ny][nx] == CLEANED:
                        continue
                    if grid[ny][nx] == WALL:
                        continue
                    queue.append((nx, ny))
                    d = i % 4
                    break
        answer = sum([grid[y][x] == 2 for x, y in product(range(m), range(n))])
        answers.append(f"{answer}")
    print(*answers, sep="\n")
