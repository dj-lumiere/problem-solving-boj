# 6930 Mod Inverse
from math import gcd

a = int(input())
b = int(input())
if gcd(a, b) != 1:
    print("No such integer exists.")
else:
    print(pow(a, -1, b))