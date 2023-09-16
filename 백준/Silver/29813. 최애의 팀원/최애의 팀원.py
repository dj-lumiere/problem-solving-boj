# 29813 최애의 팀원

from collections import deque

N = int(input())
teams = deque()
for _ in range(N):
    a, b = input().split(" ")
    b = int(b)
    teams.append((a, b))
while len(teams) > 1:
    current_student, rotate_count = teams.popleft()
    for _ in range(rotate_count % 100 - 1):
        teams.append(teams.popleft())
    teams.popleft()
print(teams[0][0])