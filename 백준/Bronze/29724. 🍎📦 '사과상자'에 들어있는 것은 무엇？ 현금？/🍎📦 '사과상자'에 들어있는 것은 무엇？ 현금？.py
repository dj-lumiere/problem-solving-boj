# 29724 🍎📦 '사과상자'에 들어있는 것은 무엇? 현금?

from functools import reduce
from sys import stdin


def input():
    return stdin.readline().strip()


box_mass = 0
apple_price_total = 0
PRICE_PER_APPLE = 4000
N = int(input())
for _ in range(N):
    box_category, *box_size = input().split(" ")
    box_size = list(map(int, box_size))
    if box_category == "B":
        box_mass += 6000
    elif box_category == "A":
        box_size = [i // 12 for i in box_size]
        apple_count = reduce(lambda x, y: x * y, box_size)
        box_mass += 1000 + apple_count * 500
        apple_price_total += PRICE_PER_APPLE * apple_count
print(box_mass)
print(apple_price_total)
