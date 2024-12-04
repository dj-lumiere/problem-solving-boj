from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        papers = []
        for _ in range(N):
            x = int(input())
            y = int(input())
            w = int(input())
            h = int(input())
            papers.append((x, y, w, h))
        grid = [[0] * 1001 for _ in range(1001)]
        for idx, (x, y, w, h) in enumerate(papers, 1):
            for i in range(x, x + w):
                for j in range(y, y + h):
                    grid[i][j] = idx
        visible = [0] * (N + 1)
        for i in range(1001):
            for j in range(1001):
                if grid[i][j] != 0:
                    visible[grid[i][j]] += 1
        for idx in range(1, N + 1):
            answer = visible[idx]
            answers.append(f"{answer}")
    print(*answers, sep="\n")