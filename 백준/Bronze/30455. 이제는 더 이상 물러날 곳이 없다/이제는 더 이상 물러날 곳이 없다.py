# 30455 이제는 더 이상 물러날 곳이 없다
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
print("Goose" if N & 1 else "Duck")