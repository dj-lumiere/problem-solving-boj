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
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        col_sum = [sum(grid[i][j] for i in range(n)) for j in range(n)]
        if sorted(set(col_sum)) == sorted(col_sum) == [-n + 1 + 2 * i for i in range(n)]:
            answer = " ".join([str((col_sum[i] + n - 1) // 2 + 1) for i in range(n)])
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")