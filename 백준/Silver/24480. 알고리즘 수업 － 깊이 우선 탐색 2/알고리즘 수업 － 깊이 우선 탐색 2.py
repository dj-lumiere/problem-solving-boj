from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(2000000)

N, M, R = list(map(int, input().split(" ")))

graph_dict = dict()

for i in range(N+1):
    graph_dict[i] = []

for i in range(M):
    s, e = list(map(int, stdin.readline().rstrip().split(" ")))
    graph_dict[s].append(e)
    graph_dict[e].append(s)

for i in range(N+1):
    if graph_dict[i]:
        graph_dict[i].sort(reverse=True)

visited:list[bool] = [False for i in range(N+1)]
visited_order:dict[int, int] = dict()

def dfs(V:list[bool],E:dict[int, list[int]],R:int):
    visited_order[R] = len(visited_order) + 1
    V[R] = True
    for i in E[R]:
        if not visited[i]:
            dfs(V,E,i)

dfs(visited, graph_dict, R)

for i in range(1, N+1):
    if i in visited_order:
        stdout.writelines(f"{visited_order[i]}\n")
    else:
        stdout.writelines("0\n")