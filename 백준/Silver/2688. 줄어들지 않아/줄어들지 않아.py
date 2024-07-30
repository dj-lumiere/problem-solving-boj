dp = [[0 for _ in range(10)] for _ in range(65)]
dp[1] = [1]*10
for i in range(2, 65):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
dp2 = [sum(v) for v in dp] 
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp2[n])