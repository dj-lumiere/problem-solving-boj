# 2579 계단 오르기
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
N = int(input().strip())
stair_value_max_dp = [0 for _ in range(N + 3)]
stair = [0 for _ in range(3)] + [int(input().strip()) for _ in range(N)]
for i in range(3, N + 3):
    stair_value_max_dp[i] = max(
        stair_value_max_dp[i - 2] + stair[i],
        stair_value_max_dp[i - 3] + stair[i - 1] + stair[i],
    )
print(f"{stair_value_max_dp[-1]}")