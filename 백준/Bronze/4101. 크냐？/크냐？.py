# 4101 크냐?

while True:
    a, b = map(int, input().split(" "))
    if a == b == 0:
        break
    else:
        print("Yes" if a > b else "No")