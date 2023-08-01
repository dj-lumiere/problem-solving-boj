# 13305 주유소

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.pop()

total_cost = 0
min_price = prices[0]

for i, (price, distance) in enumerate(zip(prices, distances)):
    if price < min_price:
        min_price = price
    total_cost += min_price * distance

print(total_cost)