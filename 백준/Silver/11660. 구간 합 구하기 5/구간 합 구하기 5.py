# 11660 구간 합 구하기 5

from sys import stdin, stdout

N, M = list(map(int, stdin.readline().strip().split(" ")))
number_list = [list(map(int, stdin.readline().strip().split(" "))) for _ in range(N)]
accumulated_sum_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1:
            accumulated_sum_list[i][j] += number_list[i - 1][j - 1]
        elif i == 1:
            accumulated_sum_list[i][j] += (
                number_list[i - 1][j - 1] + accumulated_sum_list[i][j - 1]
            )
        elif j == 1:
            accumulated_sum_list[i][j] += (
                number_list[i - 1][j - 1] + accumulated_sum_list[i - 1][j]
            )
        else:
            accumulated_sum_list[i][j] += (
                number_list[i - 1][j - 1]
                + accumulated_sum_list[i - 1][j]
                + accumulated_sum_list[i][j - 1]
                - accumulated_sum_list[i - 1][j - 1]
            )
for _ in range(M):
    x1, y1, x2, y2 = list(map(int, stdin.readline().strip().split(" ")))
    result = (
        accumulated_sum_list[x2][y2]
        - accumulated_sum_list[x2][y1 - 1]
        - accumulated_sum_list[x1 - 1][y2]
        + accumulated_sum_list[x1 - 1][y1 - 1]
    )
    stdout.writelines(f"{result}\n")
