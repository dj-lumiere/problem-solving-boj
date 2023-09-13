# 18496 Euclid’s Algorithm

from math import gcd
from sys import stdin


def input():
    return stdin.readline().strip()


d, k = map(int, input().split(" "))
result = d
tmp = k
while True:
    factor = gcd(d, tmp)
    if factor == 1:
        break
    tmp //= factor
    result *= factor

if d % 4 == 2 and k % 2 == 0 and k >= 4:
    result *= 2

print(result)