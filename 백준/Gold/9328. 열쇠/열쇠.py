from itertools import product
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = int(input())
    for hh in range(t):
        h, w = int(input()), int(input())
        grid1 = [list(input()) for _ in range(h)]
        keys = list(input())
        keys_available = set([i.upper() for i in keys])
        keys_available.discard("0")
        answer = 0
        while keys:
            current_key = keys.pop()
            visited = [[False for _ in range(w)] for _ in range(h)]
            position_stack = [(x, y) for x, y in product(range(w), range(h)) if not (
                    1 <= x < w - 1 and 1 <= y < h - 1) and not (
                    grid1[y][x] == "*" or (grid1[y][x].isupper() and grid1[y][x] not in keys_available))]
            for x, y in position_stack:
                visited[y][x] = True
                if grid1[y][x].islower() and grid1[y][x].upper() not in keys_available:
                    keys_available.add(grid1[y][x].upper())
                    keys.append(grid1[y][x])
            while position_stack:
                cx, cy = position_stack.pop()
                for dx, dy in DELTA:
                    nx, ny = cx + dx, cy + dy
                    if not is_inbound(nx, w, ny, h):
                        continue
                    if visited[ny][nx]:
                        continue
                    if grid1[ny][nx] == "*":
                        continue
                    if grid1[ny][nx].isupper() and grid1[ny][nx] not in keys_available:
                        continue
                    visited[ny][nx] = True
                    if grid1[ny][nx].islower() and grid1[ny][nx].upper() not in keys_available:
                        keys_available.add(grid1[ny][nx].upper())
                        keys.append(grid1[ny][nx])
                    position_stack.append((nx, ny))

        visited = [[False for _ in range(w)] for _ in range(h)]
        position_stack = [(x, y) for x, y in product(range(w), range(h)) if not (
                1 <= x < w - 1 and 1 <= y < h - 1) and not (
                    grid1[y][x] == "*" or (grid1[y][x].isupper() and grid1[y][x] not in keys_available))]
        eprint(position_stack)
        for x, y in position_stack:
            visited[y][x] = True
        while position_stack:
            cx, cy = position_stack.pop()
            if grid1[cy][cx] == "$":
                answer += 1
            for dx, dy in DELTA:
                nx, ny = cx + dx, cy + dy
                if not is_inbound(nx, w, ny, h):
                    continue
                if visited[ny][nx]:
                    continue
                if grid1[ny][nx] == "*":
                    continue
                if grid1[ny][nx].isupper() and grid1[ny][nx] not in keys_available:
                    continue
                visited[ny][nx] = True
                position_stack.append((nx, ny))
        answers.append(answer)
        eprint(keys_available)
    print(*answers, sep="\n")
