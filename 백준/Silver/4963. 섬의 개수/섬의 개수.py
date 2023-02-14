# 4963 섬의 개수
from sys import setrecursionlimit

setrecursionlimit(10000)
h = 0
graph = []


def dfs(pos_x, pos_y):
    if pos_x < 0 or pos_x >= w or pos_y < 0 or pos_y >= h:
        return False
    if graph[pos_y][pos_x]:
        graph[pos_y][pos_x] = 0
        dfs(pos_x, pos_y - 1)
        dfs(pos_x, pos_y + 1)
        dfs(pos_x - 1, pos_y)
        dfs(pos_x + 1, pos_y)
        dfs(pos_x - 1, pos_y - 1)
        dfs(pos_x - 1, pos_y + 1)
        dfs(pos_x + 1, pos_y - 1)
        dfs(pos_x + 1, pos_y + 1)
        return True
    return False


while True:
    if h == 0:
        w, h = list(map(int, input().split(" ")))
        if w == 0 and h == 0:
            break
    else:
        island_count = 0
        for i in range(h):
            graph.append(list(map(int, input().split(" "))))
        for y, j in enumerate(graph):
            for x, k in enumerate(j):
                island_count += dfs(x, y)
        w, h = 0, 0
        graph = []
        print(island_count)