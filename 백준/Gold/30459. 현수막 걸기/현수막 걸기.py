# 30459 현수막 걸기
from sys import stdin
from bisect import bisect_right


def input():
    return stdin.readline().strip()


differences = set()
N, M, R = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
B.sort()
is_possible = False
max_area = 0.0
for i in range(N - 1):
    for j in range(i + 1, N):
        differences.add(abs(A[i] - A[j]))
for i in differences:
    index = bisect_right(B, 2 * R / i)
    if index != 0:
        is_possible = True
        max_area = max(max_area, B[index - 1] * i / 2)
if is_possible:
    print(f"{max_area:0.1f}")
else:
    print(-1)