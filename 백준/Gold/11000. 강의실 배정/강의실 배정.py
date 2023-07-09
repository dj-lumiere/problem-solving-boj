# 11000 강의실 배정

from heapq import heappop, heappush, heapify
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
N = int(input())
class_list = [list(map(int, input().split(" "))) for _ in range(N)]
class_list = sorted(class_list, key=lambda x: (x[0], x[1] - x[0]))
start = 0
end = N + 1
while start + 1 < end:
    mid = (start + end) // 2
    divvy_up_successful = True
    room_divvy_up = [0] * mid
    heapify(room_divvy_up)
    for index, (class_start, class_end) in enumerate(class_list):
        if room_divvy_up[0] > class_start:
            divvy_up_successful = False
            break
        last_class_finish_time = room_divvy_up[0]
        heappop(room_divvy_up)
        heappush(room_divvy_up, max(last_class_finish_time, class_end))
    if divvy_up_successful:
        end = mid
    else:
        start = mid
print(f"{end}")
