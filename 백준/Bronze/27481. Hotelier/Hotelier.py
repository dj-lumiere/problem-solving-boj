# 27481 Hotelier

_ = int(input())
query = list(input())
room = [0 for _ in range(10)]
for i in query:
    if i == "L":
        for j, v in enumerate(room):
            if not v:
                room[j] = 1
                break
    elif i == "R":
        for j, v in enumerate(reversed(room), start=1):
            if not v:
                room[-j] = 1
                break
    else:
        room[int(i)] = 0
print(*room, sep="")