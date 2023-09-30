# 1269 대칭 차집합

from collections import Counter
from sys import stdin


def input():
    return stdin.readline().strip()


n, m = map(int, input().split(" "))
A = Counter(map(int, input().split(" ")))
B = Counter(map(int, input().split(" ")))
intersect = {}
for k, v in A.items():
    if k in B:
        intersect[k] = min(v, B[k])
print(n + m - 2 * sum(intersect.values()))