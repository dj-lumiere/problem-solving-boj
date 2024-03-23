a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])
if a + b <= c:
    print(0)
elif a == b == c:
    print(2)
elif a ** 2 + b ** 2 == c ** 2:
    print(1)
else:
    print(0)