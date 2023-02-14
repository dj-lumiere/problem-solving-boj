from collections import deque
from sys import stdin

N, M, V = list(map(int, input().split(" ")))

def loading_tuple_n(n: int) -> list[list[int]]:
    string_list = []
    while n:
        n -= 1
        string_element = stdin.readline().rstrip()
        string_list.append(list(map(int, string_element.split(" "))))
    return string_list

def graphify(node_count:int, connections:list[list[int]]) -> list[list[int]]:
    graph = [[] for i in range(0, node_count + 1)]
    for i in connections:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    for i in range(0, node_count + 1):
        graph[i].sort()
    return graph

def dfs(graph:list[list[int]], v: int, visited: bool):

    # 일단 시작 노드 방문 처리
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 노드를 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph:list[list[int]], v: int, visited: bool):

    visit_queue = deque()
    visit_queue.append(v)

    visited[v] = True

    while visit_queue:

        next_visit = visit_queue.popleft()
        print(next_visit, end = " ")

        for i in graph[next_visit]:
            if not visited[i]:
                visit_queue.append(i)
                visited[i] = True

visit_check = [False for i in range(0, N+1)]
target_graph = graphify(N, loading_tuple_n(M))
dfs(target_graph, V, visit_check)
print("")
visit_check = [False for i in range(0, N+1)]
bfs(target_graph, V, visit_check)