# 16956 늑대와 양
from collections import deque

y_size, x_size = list(map(int, input().split(" ")))
grid = []
for i in range(y_size):
    input_sub = input()
    grid.append([input_sub[i] for i in range(x_size)])

queue = deque()
dx_dy_list = [(-1,0),(1,0),(0,-1),(0,1)]
for x in range(x_size):
    for y in range(y_size):
        if grid[y][x] == "W":
            queue.append((x,y))

if not queue:
    for x in range(x_size):
        for y in range(y_size):
            if grid[y][x] == ".":
                grid[y][x] = "D"
    print(1)
    for i in grid:
        print("".join(i))
else:
    def bfs():
        while queue:
            x, y = queue.popleft()
            for dx, dy in dx_dy_list:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= x_size or new_y < 0 or new_y >= y_size:
                    continue
                else:
                    if grid[new_y][new_x] == "S":
                        return 0
                    if grid[new_y][new_x] == ".":
                        grid[new_y][new_x] = "D"
    code = bfs()
    if code == 0:
        print(0)
    else:
        print(1)
        for i in grid:
            print("".join(i))