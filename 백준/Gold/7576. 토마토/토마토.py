# 7576 토마토

from sys import stdin
from collections import deque

x_size, y_size = list(map(int, input().split(" ")))
graph = [list(map(int, stdin.readline().rstrip().split(" "))) for y in range(y_size)]

dx_dy_list = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    while queue:
        x,y = queue.popleft()
        for dx, dy in dx_dy_list:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= x_size or new_y < 0 or new_y >= y_size:
                continue
            if graph[new_y][new_x] == -1:
                continue
            if graph[new_y][new_x] == 0:
                graph[new_y][new_x] = graph[y][x] + 1
                queue.append((new_x, new_y))
    return graph

queue = deque()
for x in range(x_size):
    for y in range(y_size):
        # 1일 때 queue에 넣고 bfs 돌리기
        if graph[y][x] == 1:
            queue.append((x,y))
bfs()

def check_unripe_tomato() -> int:
    max_temp = 0
    for x in range(x_size):
        for y in range(y_size):
            if not graph[y][x]:
                return -1
            max_temp = max(graph[y][x]-1,max_temp)
    return max_temp

print(check_unripe_tomato())