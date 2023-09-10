# 29767 점수를 최대로

from sys import stdin


def input():
    return stdin.readline().strip()


N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
A_accsum = []
for i, v in enumerate(A):
    if i == 0:
        A_accsum.append(v)
        continue
    A_accsum.append(v + A_accsum[-1])
A_accsum.sort(reverse=True)
print(sum(A_accsum[:K]))