N, M = map(int, input().split())
s = list(map(int, input().split()))
A, D = map(int, input().split())
dp = [[0 for _ in range(N + D)] for _ in range(N + 1)]
s += [0] * (D - 1)
for i, v in enumerate(s, start=1):
    dp[0][i] = dp[0][i - 1] + v
for i in range(1, N + 1):
    for j in range(1, N + D):
        if j >= D:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + s[j - 1], dp[i - 1][j - D] + A)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + s[j - 1])
answer = -1
for i in range(N + 1):
    if dp[i][-1] >= M:
        answer = i
        break
print(answer)