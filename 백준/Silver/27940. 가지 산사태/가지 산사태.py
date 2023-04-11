# B번 - 가지 산사태

from sys import stdin

N, M, K = map(int, stdin.readline().strip().split(" "))
first_floor_rain = 0
critical_time = -1
for i in range(M):
    _, rain_amount = map(int, stdin.readline().strip().split(" "))
    first_floor_rain += rain_amount
    if first_floor_rain > K and critical_time == -1:
        critical_time = i + 1
if critical_time != -1:
    print(f"{critical_time} 1")
else:
    print(-1)
