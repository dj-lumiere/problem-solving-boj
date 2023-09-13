# 1975 Number Game

from sys import stdin


def input():
    return stdin.readline().strip()


def sol(n, b):
    o, p = n, 0
    while True:
        if o % b:
            return p
        o //= b
        p += 1


T = int(input())
for _ in range(T):
    n = int(input())
    print(sum([sol(n, b) for b in range(2, n + 1)]))