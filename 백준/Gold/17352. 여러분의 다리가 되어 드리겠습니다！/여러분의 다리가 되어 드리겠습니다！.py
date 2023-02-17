# 17352 여러분의 다리가 되어 드리겠습니다!

# DFS를 하다보면 T와 F가 경계를 가지는 지점이 생김
# 그러면 그 지점만 이어주면 됨

from sys import stdin

N = int(input())

graph = [[]] + [[] for i in range(N)]
visited = [True] + [False] * N

for _ in range(N - 2):
    i, j = list(map(int, stdin.readline().rstrip().split(" ")))
    graph[i].append(j)
    graph[j].append(i)


def dfs(init: int):
    stack = [init]
    while stack:
        next_node = stack.pop()
        visited[next_node] = True
        for i in graph[next_node]:
            if not visited[i]:
                stack.append(i)


dfs(1)

for i in range(N):
    if visited[i] and not visited[i + 1]:
        print(i, i + 1)
        break