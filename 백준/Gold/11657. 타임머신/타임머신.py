# 11657 타임머신
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
INF = 10**18

N, M = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
has_negative_cycle = False
for _ in range(M):
    init, dest, cost = map(int, input().split(" "))
    graph[init].append((dest, cost))
distance[1] = 0
for _ in range(N - 1):
    for init in range(1, N + 1):
        for dest, cost in graph[init]:
            if distance[init] != INF and distance[init] + cost < distance[dest]:
                distance[dest] = distance[init] + cost
for init in range(1, N + 1):
    for dest, cost in graph[init]:
        if distance[init] != INF and distance[init] + cost < distance[dest]:
            has_negative_cycle = True
            break
if has_negative_cycle:
    print("-1")
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            distance[i] = -1
    print(f"{chr(10).join(map(str, distance[2:]))}")