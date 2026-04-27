# 28701 세제곱의 합

from sys import stdin

input = stdin.readline
A = int(input())
x, z = 0, 0
for i in range(1, A + 1):
    x += i
    z += i**3
print(x, x**2, z, sep="\n")