from collections import deque

answers = []
INF = 10 ** 18
t = 10
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for hh in range(t):
    node_count, start = map(int, input().split())
    nodes = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for s, e in zip(nodes[::2], nodes[1::2]):
        graph[s].append(e)
    for i, v in enumerate(graph):
        graph[i] = sorted(set(v))
    visited = [0 for _ in range(101)]
    queue = deque([start])
    visited[start] = 1
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if visited[next_node]:
                continue
            visited[next_node] = visited[current_node] + 1
            queue.append(next_node)
    last_time_called = max(visited)
    answer = 0
    for i, v in enumerate(visited):
        if v == last_time_called:
            answer = i
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
