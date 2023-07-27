# 15992 1, 2, 3 더하기 7
from itertools import product

dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = dp[2][1] = dp[3][1] = 1
for i, j in product(range(1, 1001), range(2, 1001)):
    dp[i][j] = (
        (dp[i - 1][j - 1] if i >= 1 else 0)
        + (dp[i - 2][j - 1] if i >= 2 else 0)
        + (dp[i - 3][j - 1] if i >= 3 else 0)
    ) % 1_000_000_009


def solution(N: int, M: int) -> int:
    return dp[N][M]


T = int(input())
for _ in range(T):
    print(solution(*map(int, input().split(" "))))