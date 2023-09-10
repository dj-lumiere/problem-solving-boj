# U번 - 택배가 안와잉

work_start, work_end = input().split()
work_start_h, work_start_m = map(int, work_start.split(":"))
work_end_h, work_end_m = map(int, work_end.split(":"))
work_start_m = work_start_h * 60 + work_start_m
work_end_m = work_end_h * 60 + work_end_m
pre_request, request_time = map(int, input().split(" "))
max_request_per_day = (work_end_m - work_start_m) // request_time
if (work_end_m - work_start_m) % request_time == 0:
    max_request_per_day -= 1
day, remainder = divmod(pre_request + 1, max_request_per_day)
if remainder == 0:
    day -= 1
    remainder += max_request_per_day
arrive_time = work_start_m + remainder * request_time
arrive_h, arrive_m = divmod(arrive_time, 60)
print(f"{day}\n{arrive_h:0>2}:{arrive_m:0>2}")