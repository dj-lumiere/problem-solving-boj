# 1547 공

ball = [False, True, False, False]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split(" "))
    ball[x], ball[y] = ball[y], ball[x]
for index, value in enumerate(ball):
    if value:
        print(index)
        break