N = int(input())
graph:dict = {i:[] for i in range(1, N+1)}
for i in range(1, N+1):
    graph[i] = [i+1 for i, j in enumerate(list(map(int, input().split(" ")))) if j == 1]
connected:dict = {i:[0 for j in range(0,N+1)] for i in range(0,N+1)}

def dfs(init, end, visited):
    stack = [init]
    while stack:
        next_node = stack.pop()
        for i in graph[next_node]:
            stack.append(i)
            if not visited[i]:
                visited[i] = True
            else:
                stack.pop()
    return visited[end]

for i in range(1, N+1, 1):
    for j in range(1, N+1, 1):
        visited = [False for i in range(0,N+1)]
        connected[i][j] = int(dfs(i, j, visited))

for i in range(1, N+1):
    print(" ".join(list(map(str, connected[i][1:]))))