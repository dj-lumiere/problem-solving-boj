from sys import stdin

N = int(input())
M = int(input())

def loading_tuple_n(n: int) -> list[list[int]]:
    string_list = []
    while n:
        n -= 1
        string_element = stdin.readline().rstrip()
        string_list.append(list(map(int, string_element.split(" "))))
    return string_list

node_list = loading_tuple_n(M)

def graphify(node_count:int, connections:list[list[int]]) -> list[list[int]]:
    graph = [[] for i in range(0, node_count + 1)]
    for i in connections:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    for i in range(0, node_count + 1):
        graph[i].sort()
    return graph

node_graph = graphify(N, node_list)

def sol(graph: list[list[int]]) -> int:
    check = [False for i in range(0, N+1)]
    def dfs(graph, init, visited):
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
    return sum(dfs(graph, 1, check))-1

print(sol(node_graph))
