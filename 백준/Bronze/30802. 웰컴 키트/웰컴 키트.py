# 30802 웰컴 키트

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
size_list = list(map(int, input().split(" ")))
t, p = map(int, input().split(" "))
print(sum((i + t - 1) // t for i in size_list))
print(*divmod(N, p))