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
    for hh in range(t):
        n, m = int(input()), int(input())
        grid = [[int(input()) for _ in range(m)] for _ in range(n)]
        min_cost = INF
        for r in range(n):
            for c in range(m):
                total_cost = 0
                for i in range(n):
                    for j in range(m):
                        total_cost += grid[i][j] * (abs(r - i) + abs(c - j))
                if total_cost < min_cost:
                    min_cost = total_cost
        answer = f"{min_cost}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")