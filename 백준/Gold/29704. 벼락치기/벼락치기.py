# 29704 벼락치기

from sys import stdin


def input():
    return stdin.readline().strip()


N, T = map(int, input().split(" "))
task_info = [list(map(int, input().split(" "))) for _ in range(N)]
money_save = [[0 for _ in range(T + 1)] for _ in range(N)]
for i in range(N):
    for j in range(T + 1):
        if j >= task_info[i][0]:
            money_save[i][j] = max(
                money_save[i][j],
                money_save[i - 1][j],
                money_save[i - 1][j - task_info[i][0]] + task_info[i][1],
            )
        else:
            money_save[i][j] = max(money_save[i][j], money_save[i - 1][j])
print(sum(i[1] for i in task_info) - money_save[-1][-1])
