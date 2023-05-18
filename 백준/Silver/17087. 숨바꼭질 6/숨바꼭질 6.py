# 17087 숨바꼭질 6

from math import gcd

N, S = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
print(gcd(*[abs(i-S) for i in A]))