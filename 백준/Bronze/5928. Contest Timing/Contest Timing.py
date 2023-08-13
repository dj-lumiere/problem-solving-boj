# 5928 Contest Timing
from datetime import datetime, timedelta

time_cap = datetime(2011, 11, 11, 11, 11, 0)
d, h, m = map(int, input().split(" "))
time_end = datetime(2011, 11, d, h, m, 0)
duration = (time_end - time_cap) // timedelta(minutes=1)
if duration < 0:
    print(-1)
else:
    print(duration)