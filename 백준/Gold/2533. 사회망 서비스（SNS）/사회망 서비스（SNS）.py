# 2533 사회망 서비스(SNS)
from sys import stdin


def input():
    return stdin.readline().strip()


def find_post_order(start):
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
                stack.append((neighbor, False))
    return post_order, parent


def iterative_dfs(post_order):
    for node in post_order:
        early[node] = 1  # Count self as early adopter
        not_early[node] = 0  # Initially, count as not an early adopter
        for next_node in graph[node]:
            if next_node == parent[node]:
                continue
            early[node] += min(early[next_node], not_early[next_node])
            not_early[node] += early[next_node]


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    i, j = map(int, input().split(" "))
    graph[i].append(j)
    graph[j].append(i)

early = [0 for _ in range(N + 1)]
not_early = [0 for _ in range(N + 1)]

start = 1
post_order, parent = find_post_order(start)
iterative_dfs(post_order)

print(min(early[start], not_early[start]))