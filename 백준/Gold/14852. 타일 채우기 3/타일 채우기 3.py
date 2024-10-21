from sys import setrecursionlimit, stdout, stderr

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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        dp = [0 for _ in range(n + 2)]
        dp[0] = 1
        dp[1] = 2
        sum_paired = [1, 2]
        for i in range(2, n + 1):
            dp[i] = (2 * sum_paired[i - 1] + 3 * sum_paired[i - 2]) % MOD
            if i >= 4:
                dp[i] -= sum_paired[i - 4]
                dp[i] %= MOD
            sum_paired.append((sum_paired[-2] + dp[i]) % MOD)
        answers.append(dp[n])
    print(*answers, sep="\n")
