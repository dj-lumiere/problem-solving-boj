# 5585 거스름돈

coin_count = 0
coin = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())
for i, v in enumerate(coin):
    while change >= v:
        change -= v
        coin_count += 1
print(coin_count)