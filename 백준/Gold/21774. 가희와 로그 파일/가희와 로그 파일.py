# 21774 가희와 로그 파일

from datetime import datetime, timedelta
from bisect import bisect_left, bisect_right
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

BASELINE_TIME = datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0)
ONE_DAY_SECOND = 24 * 60 * 60
MAX_LEVEL = 6


def find_timedelta(time_string: str) -> int:
    date, time = time_string.split(" ")
    year, month, day = map(int, date.split("-"))
    hour, minute, second = map(int, time.split(":"))
    current_time: timedelta = (
        datetime(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
        )
        - BASELINE_TIME
    )
    return current_time.days * ONE_DAY_SECOND + current_time.seconds


def find_level_log(start: int, end: int, level: int) -> int:
    start_index: int = bisect_left(logs[level], start)
    end_index: int = bisect_right(logs[level], end)
    return end_index - start_index


def find_log_higher_than_level(start: int, end: int, level_lower_bound: int) -> int:
    result: int = 0
    for level in range(level_lower_bound, MAX_LEVEL + 1):
        result += find_level_log(start, end, level)
    return result


N, Q = map(int, input().strip().split(" "))
logs: list[list[int]] = [[] for i in range(MAX_LEVEL + 1)]
for _ in range(N):
    time, level = input().strip().split("#")
    logs[int(level)].append(find_timedelta(time))
for i in range(1, MAX_LEVEL + 1):
    logs[i].sort()
for _ in range(Q):
    start_time, end_time, level_lower_bound = input().strip().split("#")
    start_timedelta = find_timedelta(start_time)
    end_timedelta = find_timedelta(end_time)
    answer = find_log_higher_than_level(
        start_timedelta, end_timedelta, int(level_lower_bound)
    )
    print(f"{answer}\n")