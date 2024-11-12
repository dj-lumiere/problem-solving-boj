from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        sx, sy, ex, ey = (int(input()) - 1 for _ in range(4))
        visited = [[False] * 8 for _ in range(8)]
        queue = [(sx, sy, 0)]
        visited[sx][sy] = True
        while queue:
            x, y, d = queue.pop(0)
            if x == ex and y == ey:
                answer = d
                break
            for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                nx = x + dx
                ny = y + dy
                if not is_inbound(nx, 8, ny, 8):
                    continue
                if visited[nx][ny]:
                    continue
                queue.append((nx, ny, d + 1))
                visited[nx][ny] = True
        answers.append(f"{answer}")
    print(*answers, sep="\n")