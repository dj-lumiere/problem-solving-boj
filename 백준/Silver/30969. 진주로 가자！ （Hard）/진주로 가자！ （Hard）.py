# 30969 진주로 가자! (Hard)

from sys import stdin


def input():
    return stdin.readline().strip()


JINJU = "jinju"
jinju_price = 0
prices = [0 for _ in range(1002)]
N = int(input())
for _ in range(N):
    dest, price = input().split(" ")
    if dest == JINJU:
        jinju_price = int(price)
        continue
    prices[min(int(price), 1001)] += 1
print(jinju_price)
print(sum(prices[jinju_price + 1 :]))