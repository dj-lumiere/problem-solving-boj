# C번 - 규칙적인 보스돌이

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


N, M, K = map(int, input().split(" "))
dps = [int(input()) for _ in range(N)]
dps.sort(reverse=True)
dps = dps[:M][::-1]
boss_info = [list(map(int, input().split(" "))) for _ in range(K)]
boss_catch_time = [
    [boss_info[i][0] // dps[j] + (boss_info[i][0] % dps[j] != 0) for i in range(K)]
    for j in range(M)
]
boss_prize = [boss_info[i][1] for i in range(K)]
dp = [[[0 for _ in range(901)] for _ in range(K + 1)] for _ in range(M)]
for j in range(M):
    for i in range(901):
        for k in range(K):
            if i >= boss_catch_time[j][k]:
                dp[j][k + 1][i] = max(
                    dp[j][k + 1][i],
                    dp[j][k][i],
                    dp[j][k][i - boss_catch_time[j][k]] + boss_prize[k],
                )
            dp[j][k + 1][i] = max(dp[j][k + 1][i], dp[j][k][i])
print(sum(dp[j][-1][-1] for j in range(M)))