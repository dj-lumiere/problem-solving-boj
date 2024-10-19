from sys import stderr, stdout

with open(0, "r") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for hh in range(t):
        n = int(input())
        file_size = [int(input()) for _ in range(n)]
        dp = [[0] * n for _ in range(n)]
        file_size_sum = [0 for _ in range(n + 1)]
        for i, v in enumerate(file_size, start=1):
            file_size_sum[i] = file_size_sum[i - 1] + v
        for r in range(1, n):
            for i in range(n - r):
                j = i + r
                dp[i][j] = min(INF, *[dp[i][k] + dp[k + 1][j] + file_size_sum[j + 1] - file_size_sum[i] for k in
                                      range(i, j)])
        answers.append(dp[0][-1])
    print(*answers, sep="\n")