# 5575 타임 카드
from datetime import timedelta

for _ in range(3):
    worktime = list(map(int, input().split(" ")))
    work_start = timedelta(hours=worktime[0], minutes=worktime[1], seconds=worktime[2])
    work_end = timedelta(hours=worktime[3], minutes=worktime[4], seconds=worktime[5])
    worktime_second = work_end - work_start
    print(*map(int, str(worktime_second).split(":")))