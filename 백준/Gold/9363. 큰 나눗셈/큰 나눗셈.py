# 9363 큰 나눗셈
from math import gcd


T = int(input())

for i in range(1, T + 1):
    a, b = list(map(int, input().split(" ")))
    a_list = list(map(int, input().split(" ")))
    b_list = list(map(int, input().split(" ")))
    if a > b:
        b_list += [1] * (a - b)
        b = a
    else:
        a_list += [1] * (b - a)
        a = b
    numerator, denominator = 1, 1
    for x, y in zip(a_list, b_list):
        numerator *= x
        denominator *= y
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    print(f"Case #{i}: {numerator} / {denominator}")