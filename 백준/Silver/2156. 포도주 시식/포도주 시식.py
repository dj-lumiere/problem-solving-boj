# 2156 포도주 시식

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
wine_amount = [0, 0, 0] + [int(input()) for _ in range(n)]
max_wine_amount = [0 for _ in range(n + 3)]
for i in range(n + 3):
    if i < 3:
        continue
    max_wine_amount[i] = max(
        max_wine_amount[i - 1],
        max_wine_amount[i - 2] + wine_amount[i],
        max_wine_amount[i - 3] + wine_amount[i - 1] + wine_amount[i],
    )
print(f"{max(max_wine_amount)}")