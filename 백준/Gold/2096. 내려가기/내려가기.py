# 2096 내려가기

from sys import stdin

input = stdin.readline
N = int(input())
minimum_value = [[0] * 3 for _ in range(2)]
maximum_value = [[0] * 3 for _ in range(2)]
toggle = False
for i in range(N):
    line = list(map(int, input().split(" ")))
    if i == 0:
        minimum_value[toggle] = line[:]
        maximum_value[toggle] = line[:]
        continue
    for j in range(3):
        if j == 0:
            minimum_value[not toggle][j] = (
                min(minimum_value[toggle][j], minimum_value[toggle][j + 1]) + line[j]
            )
            maximum_value[not toggle][j] = (
                max(maximum_value[toggle][j], maximum_value[toggle][j + 1]) + line[j]
            )
            continue
        if j + 1 == 3:
            minimum_value[not toggle][j] = (
                min(minimum_value[toggle][j - 1], minimum_value[toggle][j]) + line[j]
            )
            maximum_value[not toggle][j] = (
                max(maximum_value[toggle][j - 1], maximum_value[toggle][j]) + line[j]
            )
            continue
        minimum_value[not toggle][j] = (
            min(
                minimum_value[toggle][j - 1],
                minimum_value[toggle][j],
                minimum_value[toggle][j + 1],
            )
            + line[j]
        )
        maximum_value[not toggle][j] = (
            max(
                maximum_value[toggle][j - 1],
                maximum_value[toggle][j],
                maximum_value[toggle][j + 1],
            )
            + line[j]
        )
    toggle ^= True
result = max(maximum_value[toggle]), min(minimum_value[toggle])
print(*result)