# 30877 X marks the Spot

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
for _ in range(N):
    S, T = input().split(" ")
    S = S.upper()
    print(T[S.index("X")].upper(), end="")
