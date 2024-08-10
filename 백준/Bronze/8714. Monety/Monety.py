n = int(input())
coin = list(map(int, input().split()))
print(min(coin.count(1), coin.count(0)))