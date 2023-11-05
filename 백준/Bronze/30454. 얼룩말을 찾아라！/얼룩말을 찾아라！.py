# A번 - 얼룩말을 찾아라!
from sys import stdin
from re import split
from collections import Counter


def input():
    return stdin.readline().strip()


N, L = map(int, input().split(" "))
stripe_count = []
for _ in range(N):
    zebra = split("[0]+", input())
    answer = 0
    for substring in zebra:
        if substring:
            answer += 1
    stripe_count.append(answer)
stripe_count_counter = Counter(stripe_count)
print(max(stripe_count), stripe_count_counter[max(stripe_count)])