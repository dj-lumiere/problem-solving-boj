# 1865 웜홀

from sys import stdin

input = stdin.readline
INF = 10**18
T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split(" "))
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    has_negative_cycle = False
    for _ in range(M):
        init, dest, cost = map(int, input().split(" "))
        graph[init].append((dest, cost))
        graph[dest].append((init, cost))
    for _ in range(W):
        init, dest, cost = map(int, input().split(" "))
        graph[init].append((dest, -cost))
    distance[1] = 0
    for _ in range(N - 1):
        for init in range(1, N + 1):
            for dest, cost in graph[init]:
                if distance[init] + cost < distance[dest]:
                    distance[dest] = distance[init] + cost
    for init in range(1, N + 1):
        for dest, cost in graph[init]:
            if distance[init] + cost < distance[dest]:
                has_negative_cycle = True
                break
    if has_negative_cycle:
        print("YES")
    else:
        print("NO")