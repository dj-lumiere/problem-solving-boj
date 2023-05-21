# 28114 팀명 정하기
from sys import stdin

teammates = []
number_of_teammates = 3
for _ in range(number_of_teammates):
    teammates.append((stdin.readline().strip().split(" ")))

for index, (solved_problems, entrance_year, surname) in enumerate(teammates):
    teammates[index] = (int(solved_problems), int(entrance_year) % 100, surname)
teammates = sorted(teammates, key=lambda x: x[1])
print(*[teammates[i][1] for i in range(number_of_teammates)], sep="")
teammates = sorted(teammates, key=lambda x: -x[0])
print(*[teammates[i][2][0] for i in range(number_of_teammates)], sep="")
