# 2748 피보나치 수 2

memo = [0, 0]

N = int(input())
for i in range(N + 1):
    if i == 0:
        memo[0] = 0
    elif i == 1:
        memo[1] = 1
    else:
        memo[i % 2] = sum(memo)
print(memo[N % 2])