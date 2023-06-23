# 2606 바이러스

from sys import stdin

input = stdin.readline


def loading_tuple_n(n: int) -> list[list[int]]:
    string_list = []
    while n:
        n -= 1
        string_element = stdin.readline().strip()
        string_list.append(list(map(int, string_element.split(" "))))
    return string_list


def graphify(node_count: int, connections: list[list[int]]) -> list[list[int]]:
    graph = [[] for i in range(0, node_count + 1)]
    for i in connections:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    for i in range(0, node_count + 1):
        graph[i].sort()
    return graph


def dfs(graph: list[list[int]], init: int) -> list[bool]:
    visited: list[bool] = [False for i in range(N + 1)]
    visited[init] = True
    stack = []
    stack.append(init)
    while stack:
        new_starting_pt = stack.pop()
        for i in graph[new_starting_pt]:
            stack.append(i)
            if not visited[i]:
                visited[i] = True
            else:
                stack.pop()
    return visited


def sol(graph: list[list[int]]) -> int:
    return sum(dfs(graph, 1)) - 1


N = int(input())
M = int(input())
node_list = loading_tuple_n(M)
node_graph = graphify(N, node_list)
print(sol(node_graph))