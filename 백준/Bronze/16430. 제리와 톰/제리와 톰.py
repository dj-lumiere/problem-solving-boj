# 16430 제리와 톰

from math import gcd

A, B = map(int, input().split(" "))
C = B - A
g = gcd(C, B)
C, B = C // g, B // g
print(C, B)