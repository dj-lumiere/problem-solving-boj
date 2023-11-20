# 2783 삼각 김밥

prices = []
x, y = map(int, input().split())
prices.append(x / y)
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    prices.append(x / y)
print(min(prices) * 1000)
