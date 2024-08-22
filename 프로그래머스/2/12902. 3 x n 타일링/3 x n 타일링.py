def solution(n):
    if n & 1:
        return 0
    n //= 2
    dp = [0 for _ in range(2501)]
    for i in range(2501):
        if i == 0:
            dp[i] = 1
            continue
        if i == 1:
            dp[i] = 3
            continue
        dp[i] = dp[i-1]
        for j in range(1, i+1):
            dp[i] += dp[i-j]*2
            dp[i] %= 1000000007
    answer = dp[n]
    return answer