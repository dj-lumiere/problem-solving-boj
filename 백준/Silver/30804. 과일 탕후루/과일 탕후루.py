# 30804 과일 탕후루
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
A = list(map(int, input().split(" ")))
total_result = 0
for i in range(1, 10):
    for j in range(i + 1, 10):
        answer = [0] * N
        for a, v in enumerate(A):
            if a == 0 and v in (i, j):
                answer[a] = 1
            elif a == 0 and v not in (i, j):
                answer[a] = 0
            elif a != 0 and v not in (i, j):
                answer[a] = 0
            else:
                answer[a] = answer[a - 1] + 1
        total_result = max(total_result, max(answer))
print(total_result)