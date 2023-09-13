# 29261 소수 세기
from sys import stdin


def input():
    return stdin.readline().strip()


P = int(input())
print((2 * ((P + 1) // 3)) - 1 if P >= 5 else 1)