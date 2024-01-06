# 17241 Pineapple Advertising

from sys import stdin


def input():
    return stdin.readline().strip()


N, M, Q = map(int, input().split())
graph = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
for _ in range(Q):
    a = int(input())
    previous_set_length = len(graph[0])
    graph[0].add(a)
    if len(graph[0]) > len(graph[a]):
        for i in graph[a]:
            graph[0].add(i)
        graph[a].clear()
    else:
        for i in graph[0]:
            graph[a].add(i)
        graph[0].clear()
        graph[0], graph[a] = graph[a], graph[0]
    print(len(graph[0]) - previous_set_length)