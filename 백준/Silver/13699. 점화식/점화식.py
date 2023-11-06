# 13699 점화식


def t(n):
    if n == 0:
        return 1
    dp = [1]
    for _ in range(1, n + 1):
        dp.append(sum(i * j for i, j in zip(dp, reversed(dp))))
    return dp[-1]


n = int(input())
print(t(n))