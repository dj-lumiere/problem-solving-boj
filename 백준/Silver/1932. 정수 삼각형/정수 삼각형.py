# 1932 정수 삼각형

n = int(input())
triangle = [list(map(int, input().split(" "))) for _ in range(n)]
maximum_path_dp = [[0] * i for i in range(1, n + 1)]
maximum_path_dp[-1] = triangle[-1]
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        maximum_path_dp[i][j] = triangle[i][j] + max(
            maximum_path_dp[i + 1][j], maximum_path_dp[i + 1][j + 1]
        )
print(maximum_path_dp[0][0])