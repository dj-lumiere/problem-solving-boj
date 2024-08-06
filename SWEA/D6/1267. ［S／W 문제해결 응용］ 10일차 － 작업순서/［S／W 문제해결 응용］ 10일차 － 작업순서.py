from collections import deque

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

answers = []
INF = 10 ** 18
t = 10
for hh in range(t):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    nodes = list(map(int, input().split()))
    for a, b in zip(nodes[::2], nodes[1::2]):
        graph[a].append(b)
    result = topological_sort(N, graph)
    answer = " ".join(map(str, result))
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
