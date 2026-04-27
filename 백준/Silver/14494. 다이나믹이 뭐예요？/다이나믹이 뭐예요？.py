import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        m = int(input())
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for c in range(n):
            for r in range(m):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] += dp[r][c - 1]
                elif c == 0:
                    dp[r][c] += dp[r - 1][c]
                else:
                    dp[r][c] += dp[r][c - 1] + dp[r - 1][c] + dp[r - 1][c - 1]
                dp[r][c] %= 1000000007
        answer = dp[-1][-1]
        answers[i] = f"{answer}"
    print(answers)