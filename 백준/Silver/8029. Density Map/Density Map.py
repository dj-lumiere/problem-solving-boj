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
        N = int(input())
        R = int(input())
        grid = [[int(input()) for _ in range(N)] for _ in range(N)]
        prefix = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            row_sum = 0
            for j in range(1, N + 1):
                row_sum += grid[i - 1][j - 1]
                prefix[i][j] = prefix[i - 1][j] + row_sum
        output = []
        for r in range(1, N + 1):
            row = []
            for c in range(1, N + 1):
                r1 = max(1, r - R)
                c1 = max(1, c - R)
                r2 = min(N, r + R)
                c2 = min(N, c + R)
                count = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
                row.append(str(count))
            answer = ' '.join(row)
            answers.append(f"{answer}")
    print(*answers, sep="\n")