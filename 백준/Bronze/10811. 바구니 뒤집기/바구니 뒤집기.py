# 10811 바구니 뒤집기

N, M = map(int, input().split(" "))
ball_number = [i for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split(" "))
    ball_number[i : j + 1] = (ball_number[i : j + 1])[::-1]
ball_number.pop(0)
print(*ball_number)