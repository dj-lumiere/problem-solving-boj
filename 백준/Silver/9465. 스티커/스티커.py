# 9465 스티커
from itertools import product
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
INVALID = -(10**9)


def max_sticker_point(n, sticker_point) -> int:
    max_point_dp = [[0 for _ in range(n)] for _ in range(2)]
    for j, i in product(range(n), range(2)):
        if j == 0:
            max_point_dp[i][j] = sticker_point[i][j]
            continue
        if j == 1:
            max_point_dp[i][j] = sticker_point[i ^ 1][j - 1] + sticker_point[i][j]
            continue
        max_point_dp[i][j] = (
            max(
                max_point_dp[i ^ 1][j - 1],
                max_point_dp[i][j - 2],
                max_point_dp[i ^ 1][j - 2],
            )
            + sticker_point[i][j]
        )
    return max(max_point_dp[i][-1] for i in range(2))


T = int(input())
for _ in range(T):
    n = int(input())
    sticker_point = [list(map(int, input().split(" "))) for _ in range(2)]
    print(f"{max_sticker_point(n, sticker_point)}\n")