from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for case_num in range(1, t + 1):
        p, q = int(input()), int(input())
        prisoners = [0] + [int(input()) for _ in range(q)] + [p + 1]
        dp = [[0] * (q + 2) for _ in range(q + 2)]
        for length in range(2, q + 2):
            for i in range(q + 2 - length):
                j = i + length
                dp[i][j] = min(dp[i][k] + dp[k][j] + (prisoners[j] - prisoners[i] - 2) for k in range(i + 1, j))
        answers.append(f"Case #{case_num}: {dp[0][q + 1]}")
    print(*answers, sep="\n")