# 8679 Zbiór

from sys import stdin


def input():
    return stdin.readline().strip()


n = int(input())
for _ in range(n):
    a, b = map(int, input().split(" "))
    if b % a:
        print("NIE")
    else:
        print("TAK")