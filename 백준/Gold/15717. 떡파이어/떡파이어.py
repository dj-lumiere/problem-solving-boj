# 15717 떡파이어

MOD = 10**9 + 7
n = int(input())
if not n:
    print(1)
else:
    print(pow(2, n - 1, MOD))