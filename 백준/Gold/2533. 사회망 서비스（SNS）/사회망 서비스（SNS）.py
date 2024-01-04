# 2533 사회망 서비스(SNS)
from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)


def input():
    return stdin.readline().strip()


def dfs(current_node):
    visited[current_node] = True
    early[current_node] = 1
    not_early[current_node] = 0
    for next_node in graph[current_node]:
        if visited[next_node]:
            continue
        dfs(next_node)
        early[current_node] += min(early[next_node], not_early[next_node])
        not_early[current_node] += early[next_node]


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    i, j = map(int, input().split(" "))
    graph[i].append(j)
    graph[j].append(i)

early = [0 for _ in range(N + 1)]
not_early = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
start = 1
dfs(start)
print(min(early[start], not_early[start]))