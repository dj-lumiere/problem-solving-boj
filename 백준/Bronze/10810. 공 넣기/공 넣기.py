# 10810 공 넣기

N, M = map(int, input().split(" "))
ball_number = [0 for _ in range(N + 1)]
for _ in range(M):
    i, j, k = map(int, input().split(" "))
    ball_number[i : j + 1] = [k] * (j + 1 - i)
ball_number.pop(0)
print(*ball_number)