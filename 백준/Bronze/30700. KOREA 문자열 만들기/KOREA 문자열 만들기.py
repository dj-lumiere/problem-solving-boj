# 30700 KOREA 문자열 만들기

S = list(input())
dp = [-1] * len(S)
target = "KOREA"
for i, v in enumerate(dp):
    if i == 0 and target[(v + 1) % 5] == S[i]:
        dp[i] += 1
    elif i > 0 and target[(dp[i - 1] + 1) % 5] == S[i]:
        dp[i] = dp[i - 1] + 1
    elif i > 0:
        dp[i] = dp[i - 1]
print(dp[-1] + 1)