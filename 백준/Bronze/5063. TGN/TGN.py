# 5063 TGN

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split(" "))
    difference = r - (e - c)
    if difference > 0:
        print("do not advertise")
    elif difference == 0:
        print("does not matter")
    elif difference < 0:
        print("advertise")