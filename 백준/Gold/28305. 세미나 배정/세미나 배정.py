# 28305 세미나 배정

from heapq import heappop, heappush, heapify

N, T = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
a.sort()
start = 0
end = N + 1
while start + 1 < end:
    mid = (start + end) // 2
    divvy_up_successful = True
    room_divvy_up = [0] * mid
    heapify(room_divvy_up)
    for index, value in enumerate(a):
        if room_divvy_up[0] >= value:
            divvy_up_successful = False
            break
        last_seminar_finish_time = room_divvy_up[0]
        heappop(room_divvy_up)
        heappush(room_divvy_up, max(value, last_seminar_finish_time + T))
    if divvy_up_successful:
        end = mid
    else:
        start = mid
print(end)
