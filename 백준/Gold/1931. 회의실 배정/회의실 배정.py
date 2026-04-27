# 1931 회의실 배정
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
N = int(input())
meeting_rooms = []
for index in range(N):
    start, end = map(int, input().split())
    meeting_rooms.append((start, end))
meeting_rooms.sort(key=lambda x: (x[1], x[0]))
# 시작 시간 중 제일 짧은 회의시간을 찾음
last_end_time = 0
count = 0
for meeting_room in meeting_rooms:
    # 그 다음 시간 중 제일 거리가 짧은 시작시간 찾음
    if meeting_room[0] >= last_end_time:
        last_end_time = meeting_room[1]
        count += 1
print(f"{count}")