# 20500 Ezreal 여눈부터 가네 ㅈㅈ

MOD = 1_000_000_007
N = int(input())
result = [[0 for _ in range(15)] for _ in range(N)]
result[0][1] = result[0][5] = 1
for i in range(1, N):
    for j in range(15):
        for k in (1, 5):
            result[i][((10*j)+k) % 15] += result[i-1][j]
            result[i][((10*j)+k) % 15] %= MOD
print(result[-1][0])