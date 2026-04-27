from math import isqrt

t = int(input())
for _ in range(t):
    x = input()
    if int(x) == isqrt(int(x))**2 and int(x[::-1]) == isqrt(int(x[::-1]))**2:
        print("YES")
    else:
        print("NO")