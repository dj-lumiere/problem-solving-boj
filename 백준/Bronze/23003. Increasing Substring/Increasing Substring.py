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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        s = input()
        dp = [1] * n
        for i in range(1, n):
            if s[i] > s[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        answer = ' '.join(map(str, dp))
        answers.append(f"Case #{hh}: {answer}")
    print(*answers, sep="\n")