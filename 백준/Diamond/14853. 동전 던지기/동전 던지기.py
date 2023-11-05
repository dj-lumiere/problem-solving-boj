# 14853 동전 던지기
from sys import stdin


def input():
    return stdin.readline().strip()


def solution(n1, m1, n2, m2):
    base_case = 1.0
    answer = 0.0
    for i in range(0, m1 + 1):
        base_case = base_case * (n1 + 1 - i) / (n1 + n2 + 2 - i)
    answer += base_case
    for i in range(1, m2 + 1):
        base_case = base_case * (m1 + i) / i * (n2 + 2 - i) / (n1 + n2 - m1 + 2 - i)
        answer += base_case
    return answer


T = int(input())
for _ in range(T):
    n1, m1, n2, m2 = map(int, input().split(" "))
    print(solution(n1, m1, n2, m2))