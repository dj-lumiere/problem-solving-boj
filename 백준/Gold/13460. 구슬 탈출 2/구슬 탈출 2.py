from collections import deque
from itertools import product
from sys import stderr, stdout


def move(x, y, dx, dy, grid):
    count = 0
    while True:
        if grid[y + dy][x + dx] == "#":
            break
        x += dx
        y += dy
        count += 1
        if grid[y][x] == "O":
            break
    return x, y, count


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
    t = 1
    for hh in range(t):
        n, m = int(input()), int(input())
        grid = [list(input()) for _ in range(n)]
        rx, ry = [[x, y] for x, y in product(range(m), range(n)) if grid[y][x] == "R"][0]
        bx, by = [[x, y] for x, y in product(range(m), range(n)) if grid[y][x] == "B"][0]
        grid[ry][rx] = "."
        grid[by][bx] = "."
        answer = -1
        queue = deque([(rx, ry, bx, by, 0)])
        visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
        visited[by][bx][ry][rx] = True
        while queue:
            crx, cry, cbx, cby, movement = queue.popleft()
            if movement >= 10:
                continue
            for dx, dy in DELTA:
                nrx, nry, rc = move(crx, cry, dx, dy, grid)
                nbx, nby, bc = move(cbx, cby, dx, dy, grid)
                if grid[nby][nbx] == "O":
                    continue
                if grid[nry][nrx] == "O":
                    answer = movement + 1
                    queue.clear()
                    break
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if visited[nby][nbx][nry][nrx]:
                    continue
                visited[nby][nbx][nry][nrx] = True
                queue.append((nrx, nry, nbx, nby, movement + 1))
        answers.append(answer)
    print(*answers, sep="\n")
