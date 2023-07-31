# 17404 RGB거리 2
from itertools import product
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
INVALID = 10**9
N = int(input())
price = [list(map(int, input().split(" "))) for _ in range(N)]
price_dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N)]

for first_color, current_house, current_color in product(range(3), range(N), range(3)):
    if current_house == 0 and first_color == current_color:
        price_dp[current_house][first_color][current_color] = price[current_house][
            first_color
        ]
        continue
    if current_house == 0 and first_color != current_color:
        price_dp[current_house][first_color][current_color] = INVALID
        continue
    price_dp[current_house][first_color][current_color] = (
        min(
            price_dp[current_house - 1][first_color][i]
            for i in range(3)
            if i != current_color
        )
        + price[current_house][current_color]
    )
    if current_house + 1 == N and first_color == current_color:
        price_dp[current_house][first_color][current_color] = INVALID
print(f"{min(price_dp[-1][i][j] for i, j in product(range(3), range(3)))}")