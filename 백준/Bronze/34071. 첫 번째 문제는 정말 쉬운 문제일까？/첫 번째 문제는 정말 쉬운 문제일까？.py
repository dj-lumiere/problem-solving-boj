x = int(input())
a = [int(input()) for _ in range(x)]
if max(a) == a[0]:
    print("hard")
elif min(a) == a[0]:
    print("ez")
else:
    print("?")