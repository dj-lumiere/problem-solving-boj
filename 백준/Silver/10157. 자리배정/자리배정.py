from collections import deque
from decimal import getcontext
from itertools import product
from math import floor, log10
from sys import stdout, stderr

getcontext().prec = 1000


class MapIndex:
    def __init__(self, function, iterable):
        self.function = function
        self.iterable = iterable

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, key):
        return self.function(self.iterable[key])


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        c, r, k = (int(input()) for _ in range(3))
        grid = [[0 for _ in range(c)] for _ in range(r)]
        grid[0][0] = 1
        queue = deque([(0, 0)])
        d = 0
        while queue:
            cx, cy = queue.popleft()
            if all(not is_inbound(cx + dx, c, cy + dy, r) or grid[cy + dy][cx + dx] != 0 for dx, dy in DELTA):
                break
            dx, dy = DELTA[d]
            nx, ny = cx + dx, cy + dy
            if not is_inbound(nx, c, ny, r) or grid[ny][nx] != 0:
                d += 1
                d %= 4
                queue.append((cx, cy))
                continue
            grid[ny][nx] = grid[cy][cx] + 1
            queue.append((nx, ny))
        answer = 0 if k > r * c else [f"{x + 1} {y + 1}" for x, y in product(range(c), range(r)) if grid[y][x] == k][0]
        answers.append(f"{answer}")
    print(*answers, sep="\n")