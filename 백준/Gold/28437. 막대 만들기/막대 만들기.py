# 28437 막대 만들기

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input())
A = list(map(int, input().split(" ")))
Q = int(input())
L = list(map(int, input().split(" ")))
limit = 100000
dp = [0] * (limit + 1)
for v in A:
    dp[v] += 1
for i in range(1, limit + 1):
    for j in range(2 * i, limit + 1, i):
        dp[j] += dp[i]
print(f"{' '.join(map(str, [dp[v] for v in L]))}")