while True:
    a, b = list(map(int, input().split(" ")))
    if not (a and b):
        break
    else:
        print(a+b)