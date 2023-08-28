# 10895 Great Pow!

a, k = map(int, input().split(" "))
if not a & 1 and k != 0:
    print(1)
else:
    print(a)