import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for i in range(t):
        c, v, l = [int(input()) for _ in range(3)]
        # 길이 i+1인데 끝이 자음이면 0, 모음이면 1
        dp = [[0 for _ in range(2)] for _ in range(l)]
        dp[0][0] = c
        dp[0][1] = v
        for j in range(l):
            if j == 0:
                continue
            dp[j][0] = dp[j - 1][1] * c % MOD
            dp[j][1] = (dp[j - 1][0] * v + dp[j - 1][1] * v) % MOD
        answer = dp[-1][1] % MOD
        answers[i] = f"Case #{i + 1}: {answer}"
    print(answers)