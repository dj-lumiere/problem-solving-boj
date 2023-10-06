# 1005 ACM Craft
# 적당히 정렬을 해서 트리 형태로 만든 다음 build_time_sub를 적용하기...인데...
# 정렬은 위상정렬로 하고 그 다음 이제 뭐함?

from collections import deque
from sys import stdin


def input():
    return stdin.readline().strip()


def topological_sort(n, graph):
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            indegree[j] += 1
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return result


def min_time_to_build(n, build_time, graph, w):
    order = topological_sort(n, graph)
    build_time_sub = [0] * (n + 1)
    for i in order:
        build_time_sub[i] += build_time[i]
        for j in graph[i]:
            build_time_sub[j] = max(build_time_sub[j], build_time_sub[i])
    return build_time_sub[w]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
    w = int(input())
    print(min_time_to_build(n, build_time, graph, w))