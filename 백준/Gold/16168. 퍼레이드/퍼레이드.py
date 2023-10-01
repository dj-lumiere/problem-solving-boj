# 16168 퍼레이드

from sys import stdin


def input():
    return stdin.readline().strip()


vertex_count, edge_count = map(int, input().split(" "))
graph = [[] for _ in range(vertex_count + 1)]
for _ in range(edge_count):
    start, end = map(int, input().split(" "))
    graph[start].append(end)
    graph[end].append(start)
visited = [False for _ in range(vertex_count + 1)]
stack = [1]
visited[0] = visited[1] = True
while stack:
    current_node = stack.pop()
    for next_node in graph[current_node]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        stack.append(next_node)
all_node_connected = all(visited)
node_with_odd_edges = sum(len(i) & 1 for i in graph)
print("YES" if node_with_odd_edges in (0, 2) and all_node_connected else "NO")