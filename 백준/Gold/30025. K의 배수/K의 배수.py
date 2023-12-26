# 30025 K의 배수

MOD = 10**9 + 7
N, M, K = map(int, input().split())
# dp[mod][digit_count] = 해당하는 개수
dp = [[0 for _ in range(K)] for _ in range(M + 1)]
numbers = list(map(int, input().split()))
for i in numbers:
    if i == 0:
        continue
    dp[1][i % K] += 1

for i in range(1, M):
    for j in range(K):
        for k in numbers:
            dp[i + 1][(10 * j + k) % K] += dp[i][j]
            dp[i + 1][(10 * j + k) % K] %= MOD

print(dp[-1][0])
