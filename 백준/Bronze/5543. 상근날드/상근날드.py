# 5543 상근날드

from itertools import product

burger_list = [int(input()) for _ in range(3)]
beverage_list = [int(input()) for _ in range(2)]

cheapest_price = 10000

for i, j in product(burger_list, beverage_list):
    if i + j - 50 < cheapest_price:
        cheapest_price = i + j - 50
print(cheapest_price)