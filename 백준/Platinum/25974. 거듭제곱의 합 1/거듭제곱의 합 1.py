# 25974 거듭제곱의 합 1
from math import factorial
from sys import setrecursionlimit

setrecursionlimit(10**9)

n, p = list(map(int, input().split(" ")))
modulo = 10**9 + 7
dp = [0 for _ in range(0, p + 1)]
power = [1 for _ in range(0, p + 2)]
for i in range(1, p + 2):
    power[i] = power[i - 1] * (n + 1) % modulo
dp[0] = n
dp_list = [[1 for i in range(j + 1)] for j in range(p + 2)]

for i in range(2, p+2):
    for j in range(1, i):
        dp_list[i][j] = dp_list[i-1][j-1] + dp_list[i-1][j] % modulo


def nCr(n: int, r: int) -> int:
    return dp_list[n][r]


def eea(a: int, b: int, d: int) -> list[int]:
    # (x(0),y(0)) = (1,0), (x(1),y(1)) = (0,1)
    x_y_seq_memo: list[list[int]] = [[1, 0], [0, 1]]
    # r(0) = a, r(1) = b
    r_memo: list[int] = [a, b]
    q_i: int = 0
    i: int = 2
    while True:
        # q(i+2) = r(i)//r(i+1)
        q_i = r_memo[(i - 2) % 2] // r_memo[(i - 1) % 2]
        # r(i+2) = r(i)//r(i+1)
        r_memo[i % 2] = r_memo[(i - 2) % 2] % r_memo[(i - 1) % 2]
        # (x(i+2),y(i+2))=(x(i)-x(i+1)*q(i+2),y(i)-y(i+1)*q(i+2))
        for j in range(2):
            x_y_seq_memo[i % 2][j] = (
                x_y_seq_memo[(i - 2) % 2][j] - x_y_seq_memo[(i - 1) % 2][j] * q_i
            )
        if r_memo[i % 2] == d:
            break
        else:
            i += 1
    return x_y_seq_memo[i % 2]

for i in range(1, p + 1):
    result = power[i + 1] - 1
    for j in range(0, i):
        result -= nCr(i + 1, j) * dp[j] % modulo
    result *= eea(i + 1, modulo, 1)[0]
    result %= modulo
    dp[i] = result
print(dp[p] % modulo)