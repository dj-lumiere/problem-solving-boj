# C번 - 크레이지 타임
N = int(input())
current_time = 12
prev_clock_type = ""
time_reverse = False
for i in range(1, N+1):
    desk_pound = False
    clock_type, sync_time = list(map(str, input().split(" ")))
    if time_reverse:
        current_time -= 1
    else:
        current_time += 1
    if current_time > 12:
        current_time = 1
    elif current_time < 1:
        current_time = 12
    if current_time == int(sync_time) and clock_type != "HOURGLASS":
        desk_pound = True
        print(f"{current_time} YES")
    elif current_time != int(sync_time) and clock_type == "HOURGLASS":
        if not time_reverse:
            time_reverse = True
        else:
            time_reverse = False
        print(f"{current_time} NO")
    else:
        print(f"{current_time} NO")
    prev_clock_type = clock_type