# 1247 부호

from sys import stdin


def input():
    return stdin.readline().strip()


def sign(target):
    if target > 0:
        return "+"
    elif target == 0:
        return "0"
    else:
        return "-"


for _ in range(3):
    n = int(input())
    print(sign(sum(int(input()) for _ in range(n))))