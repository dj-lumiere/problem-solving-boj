# 2178 미로 탐색

from collections import deque

y_size, x_size = list(map(int, input().split(" ")))
graph = []

for i in range(y_size):
    graph_row = []
    graph_row_str = input()
    for j in range(x_size):
        graph_row.append(int(graph_row_str[j]))
    graph.append(graph_row)

dx_dy_list = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for dx, dy in dx_dy_list:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= x_size or new_y < 0 or new_y >= y_size:
                continue
            if graph[new_y][new_x] == 0:
                continue
            if graph[new_y][new_x] == 1:
                graph[new_y][new_x] = graph[y][x] + 1
                queue.append((new_x, new_y))
    return graph[y_size-1][x_size-1]

print(bfs(0,0))