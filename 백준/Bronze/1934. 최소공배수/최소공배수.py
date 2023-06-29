# 1934 최소공배수

from math import lcm

t = int(input())
for _ in range(t):
    a, b = map(int, input().split(" "))
    print(lcm(a, b))