N: int = int(input())
matrix_size: list[tuple[int, int]] = [
    tuple(map(int, input().split())) for _ in range(N)
]

dp: list[list[int]] = [[0] * N for _ in range(N)]

for r in range(1, N):
    for i in range(N - r):
        j = i + r
        dp[i][j] = min(
            2**31, # 제일 최악으로 계산해도 2**31 - 1을 넘기지 않는다는 게 보장되어있으므로, 2 ** 31을 최대로 설정
            *[
                dp[i][k] # A(1)~A(k)까지 곱할 때 곱셈횟수
                + dp[k + 1][j] # A(k+1)~A(n)까지 곱할 때 곱셈횟수
                + matrix_size[i][0] * matrix_size[k][1] * matrix_size[j][1] # A(1)~A(k)까지의 곱과 A(k+1)~A(n)까지의 곱을 곱할 때 곱셈횟수
                for k in range(i, j)
            ],
        )

print(dp[0][N - 1])