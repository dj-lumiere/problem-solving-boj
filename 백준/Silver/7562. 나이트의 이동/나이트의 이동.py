# 7562 나이트의 이동
from collections import deque

t = int(input())
for i in range(t):
    N = int(input())
    init = list(map(int, input().split(" ")))
    target = list(map(int, input().split(" ")))
    grid = [[0 for i in range(N)] for i in range(N)]
    grid[init[1]][init[0]] = 1
    queue = deque()
    queue.append(tuple(init))
    dx_dy_list = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]
    def bfs():
        while queue:
            x,y = queue.popleft()
            for dx, dy in dx_dy_list:
                new_x = x+dx
                new_y = y+dy
                if new_x<0 or new_x>=N or new_y<0 or new_y>=N:
                    continue
                if grid[new_y][new_x] == 0:
                    grid[new_y][new_x] = grid[y][x] + 1
                    queue.append((new_x,new_y))
                    if new_x == target[0] and new_y == target[1]:
                        return
    bfs()
    print(grid[target[1]][target[0]]-1)
