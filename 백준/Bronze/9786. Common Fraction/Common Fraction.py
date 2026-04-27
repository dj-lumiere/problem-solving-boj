from math import gcd

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(a,b)
    print(a//g, b//g)