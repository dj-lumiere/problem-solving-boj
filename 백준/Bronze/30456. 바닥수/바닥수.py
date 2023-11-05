# C번 - 바닥수
from sys import stdin


def input():
    return stdin.readline().strip()


N, L = map(int, input().split(" "))
print(f"{'1'*(L-1)}{N}")