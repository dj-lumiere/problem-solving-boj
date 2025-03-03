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
        n = int(input())
        answer = 0
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        k = int(input())
        d = [int(input()) for _ in range(k)]
        d.sort(reverse=True)
        d_accsum = [0]
        for i, v in enumerate(d):
            d_accsum.append(d_accsum[-1] + v)
        grid_accsum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        blank_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i, v in enumerate(grid):
            for j, v2 in enumerate(v):
                grid_accsum[i + 1][j + 1] += v2
                blank_sum[i + 1][j + 1] += +(v2 == 0)
        for i, v in enumerate(grid_accsum):
            for j, v2 in enumerate(v):
                if i == 0:
                    continue
                grid_accsum[i][j] += grid_accsum[i - 1][j]
                blank_sum[i][j] += blank_sum[i - 1][j]
        for i, v in enumerate(grid_accsum):
            for j, v2 in enumerate(v):
                if j == 0:
                    continue
                grid_accsum[i][j] += grid_accsum[i][j - 1]
                blank_sum[i][j] += blank_sum[i][j - 1]
        for i in range(1, n + 1):
            for y in range(n - i + 1):
                for x in range(n - i + 1):
                    blank_count = blank_sum[y + i][x + i] - blank_sum[y][x + i] - blank_sum[y + i][x] + blank_sum[y][x]
                    if blank_count > k:
                        continue
                    grid_sum = grid_accsum[y + i][x + i] - grid_accsum[y][x + i] - grid_accsum[y + i][x] + \
                               grid_accsum[y][x] + d_accsum[blank_count]
                    answer = max(answer, grid_sum)
        answers.append(answer)
    print(*answers, sep="\n")