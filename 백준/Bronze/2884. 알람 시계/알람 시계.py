# 2884 알람 시계

H, M = list(map(int, input().split(" ")))

time_convert = H * 60 + M
alarm_time = (time_convert - 45) % 1440
print(" ".join(map(str, divmod(alarm_time, 60))))