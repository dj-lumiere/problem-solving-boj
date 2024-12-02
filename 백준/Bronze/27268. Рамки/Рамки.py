from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
    for _ in range(t):
        h, w, n = int(input()), int(input()), int(input())
        grid = [['.' for _ in range(w)] for _ in range(h)]
        for i in range(n):
            r1, c1, r2, c2 = int(input()), int(input()), int(input()), int(input())
            char = chr(ord('a') + i)
            for c in range(c1 - 1, c2):
                grid[r1 - 1][c] = char
                grid[r2 - 1][c] = char
            for r in range(r1 - 1, r2):
                grid[r][c1 - 1] = char
                grid[r][c2 - 1] = char
        result = '\n'.join([''.join(row) for row in grid])
        answer = result
        answers.append(f"{answer}")
    print(*answers, sep="\n")