# 2702 초6 수학
from math import gcd, lcm

T = int(input())
for _ in range(T):
    a, b = map(int, input().split(" "))
    print(lcm(a, b), gcd(a, b))