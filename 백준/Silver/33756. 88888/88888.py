n = int(input())
for _ in range(n):
    x = int(input())
    if x % 8 != 0:
        print("No")
        continue
    x //= 8
    if any(i == "9" for i in str(x)):
        print("No")
        continue
    if any(i > j for i, j in zip(str(x), str(x)[1:])):
        print("No")
        continue
    print("Yes")