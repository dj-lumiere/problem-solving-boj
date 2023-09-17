# D번 - 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다

N, M = map(int, input().split(" "))
vtuber_broadcast_list: dict[str, list[list[int]]] = {}
for _ in range(N):
    name, day, broadcast_start, broadcast_end = input().strip().split(" ")
    day = int(day) - 1
    broadcast_start_h, broadcast_start_m = map(int, broadcast_start.split(":"))
    broadcast_end_h, broadcast_end_m = map(int, broadcast_end.split(":"))
    broadcast_start = broadcast_start_h * 60 + broadcast_start_m
    broadcast_end = broadcast_end_h * 60 + broadcast_end_m
    if name not in vtuber_broadcast_list:
        vtuber_broadcast_list[name] = [[0, 0] for _ in range(M // 7)]
    vtuber_broadcast_list[name][day // 7][0] += 1
    vtuber_broadcast_list[name][day // 7][1] += broadcast_end - broadcast_start

answer = []
for k, v in vtuber_broadcast_list.items():
    if all([v[i][0] >= 5 and v[i][1] >= 3600 for i in range(M // 7)]):
        answer.append(k)
answer.sort()
if answer:
    print(*answer, sep="\n")
else:
    print(-1)