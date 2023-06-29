# 10813 공 바꾸기

N, M = map(int, input().split(" "))
ball_number = [i for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split(" "))
    ball_number[i], ball_number[j] = ball_number[j], ball_number[i]
ball_number.pop(0)
print(*ball_number)