# 29720 그래서 님 푼 문제 수가?
from sys import stdin


def input():
    return stdin.readline().strip()


n, m, k = map(int, input().split())
currently_solved_minimum = max(n - m * k, 0)
currently_solved_maximum = max(n - m * k + m - 1, 0)
print(currently_solved_minimum, currently_solved_maximum)