# 29715 비밀번호 찾기

from math import factorial
from sys import stdin


def input():
    return stdin.readline().strip()


N, M = map(int, input().split(" "))
X, Y = map(int, input().split(" "))
correct_digit, wrong_digit, no_info = 0, 0, 0
for _ in range(M):
    info, _ = map(int, input().split(" "))
    if info:
        correct_digit += 1
    else:
        wrong_digit += 1
no_info = N - correct_digit - wrong_digit
possible_password_count = factorial(wrong_digit + no_info) * (
    factorial(9 - correct_digit - wrong_digit)
    // factorial(9 - correct_digit - wrong_digit - no_info)
    // factorial(no_info)
)
time = ((possible_password_count + 2) // 3 - 1) * (3 * X + Y) + (
    possible_password_count % 3 * X if possible_password_count % 3 else 3 * X
)
print(time)
