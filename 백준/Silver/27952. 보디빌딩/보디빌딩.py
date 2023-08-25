# 27952 보디빌딩
from sys import stdin


def input():
    return stdin.readline().strip()


N, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
B_acc_sum = []
for i,v in enumerate(B):
    if i == 0:
        B_acc_sum.append(v)
        continue
    B_acc_sum.append(B_acc_sum[-1]+v)
paused_prematurely = False
for v1, v2 in zip(A, B_acc_sum):
    if v2 < v1:
        paused_prematurely = True
        break
if paused_prematurely:
    print(-1)
else:
    print((B_acc_sum[-1]-A[-1])//X)