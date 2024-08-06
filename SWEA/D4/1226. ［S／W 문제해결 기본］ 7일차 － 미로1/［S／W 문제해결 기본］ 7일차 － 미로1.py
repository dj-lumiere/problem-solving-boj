from collections import deque
from itertools import product

is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
answers = []
INF = 10 ** 18
t = 10
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for hh in range(t):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(16)]
    start = [(x, y) for x, y in product(range(16), repeat=2) if grid[y][x] == 2][0]
    end = [(x, y) for x, y in product(range(16), repeat=2) if grid[y][x] == 3][0]
    grid[end[1]][end[0]] = 0
    is_reachable = 0
    queue = deque([start])
    grid[start[1]][start[0]] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if not is_inbound(nx, 16, ny, 16):
                continue
            if grid[ny][nx] == 1:
                continue
            grid[ny][nx] = 1
            queue.append((nx, ny))
    if grid[end[1]][end[0]] == 1:
        is_reachable = 1
    answer = is_reachable
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")