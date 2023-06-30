# 2460 지능형 기차 2

person_on_station = []
current_person = 0
for _ in range(10):
    left, board = map(int, input().split(" "))
    current_person += board - left
    person_on_station.append(current_person)
print(max(person_on_station))