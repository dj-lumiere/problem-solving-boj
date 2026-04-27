N, A, B, C, D, E, F = map(int, input().split())
hobbies = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[A + i * F for _ in range(C + 1)] for i in range(B + 1)]

for i in range(1, B + 1):
    for j in range(1, C + 1):
        for a, (l, h, m) in enumerate(hobbies, start=1):
            # If we have enough time and stamina for the current hobby
            if i - h >= 0 and j - m >= 0:
                relief = l
                # Check if stamina is below threshold
                if C - (j - m) <= D:
                    relief = relief * (100 - E) // 100
                dp[i][j] = max(min(
                    dp[i][j], dp[i][j - 1], dp[i - 1][j] + F, dp[i - h][j - m] - relief), 0)
                continue
            dp[i][j] = max(min(dp[i][j], dp[i][j - 1], dp[i - 1][j] + F), 0)
print(dp[-1][-1])
