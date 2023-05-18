# 2530 인공지능 시계

H, M, S = list(map(int, input().split(" ")))
T = int(input())
time1 = (H * 60 + M) * 60 + S
time2 = time1 + T
M, S = divmod(time2, 60)
H, M = divmod(M, 60)
H %= 24
print(H, M, S, sep=" ")