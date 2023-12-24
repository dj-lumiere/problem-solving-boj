# A번 - 진주로 가자! (Easy)

from sys import stdin


def input():
    return stdin.readline().strip()

JINJU = "jinju"
jinju_price = 0
prices = []
N = int(input())
for _ in range(N):
    dest, price = input().split(" ")
    if dest == JINJU:
        jinju_price = int(price)
        continue
    prices.append(int(price))
print(jinju_price)
print(sum(i>jinju_price for i in prices))