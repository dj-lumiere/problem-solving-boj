# 23089 사탕나무
from sys import stdin


def input():
    return stdin.readline().strip()


def find_post_order(start, graph):
    N = len(graph) - 1
    stack = [(start, False)]
    post_order = []
    visited = [False for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]  # To keep track of the parent of each node

    while stack:
        node, current_node_visited = stack.pop()
        if current_node_visited:
            post_order.append(node)
            continue
        stack.append((node, True))
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                stack.append((neighbor, False))
    return post_order, parent


def find_pre_order(start, graph):
    N = len(graph) - 1
    stack = [start]
    pre_order = []
    visited = [False for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]  # To keep track of the parent of each node

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            pre_order.append(node)

            # Add children to stack (in reverse order to maintain correct traversal)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    parent[neighbor] = node
                    stack.append(neighbor)
    return pre_order


N, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
post_order, parent = find_post_order(1, graph)
pre_order = find_pre_order(1, graph)
dp = [[1 if i else 0 for i in range(N + 1)] for _ in range(K + 1)]
for i in range(1, K + 1):
    for j in post_order:
        if not parent[j]:
            continue
        dp[i][parent[j]] += dp[i - 1][j]
tmp = [[dp[j][i] for i in range(N + 1)] for j in range(K - 1)]
for i in range(1, K + 1):
    for j in pre_order:
        if i == 1 and parent[j]:
            dp[i][j] += 1
            continue
        if parent[j]:
            dp[i][j] += dp[i - 1][parent[j]] - tmp[i - 2][j]
    # print(*dp, sep="\n")
    # print()
# print(*dp, sep="\n")
# print()
print(max(dp[-1]))
