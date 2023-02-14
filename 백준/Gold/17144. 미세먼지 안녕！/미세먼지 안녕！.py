# 17144 미세먼지 안녕!
from collections import deque
y_size, x_size, time = list(map(int, input().split(" ")))
grid = [list(map(int, input().split(" "))) for y in range(y_size)]
new_grid = [[0 for x in range(x_size)] for y in range(y_size)]

air_cleaner = []
for x in range(x_size):
        for y in range(y_size):
            if grid[y][x] == -1:
                air_cleaner.append((x,y))

while time:
    time -= 1
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    queue = deque()
    for x in range(x_size):
        for y in range(y_size):
            if grid[y][x] > 0:
                queue.append((x,y))

    dx_dy_list = [(-1,0),(1,0),(0,-1),(0,1)]
    def air_diffusion():
        while queue:
            x, y = queue.popleft()
            diffusion_direction_counter = 0
# 2. (r,c)에 있는 미세먼지는 인접한 네 방향으로 확산된다. 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
            for i in dx_dy_list:
                dx, dy = i
                new_x = x+dx
                new_y = y+dy
                if new_x < 0 or new_x >= x_size or new_y < 0 or new_y >= y_size:
                    continue
                if grid[new_y][new_x] == -1:
                    continue
# 3. 확산되는 양은 A(r,c)//5이다.
                new_grid[new_y][new_x] += grid[y][x] // 5
                diffusion_direction_counter += 1
# 4. (r, c)에 남은 미세먼지의 양은 A(r,c) - (A(r,c)//5)*(확산된 방향의 개수) 이다.
            new_grid[y][x] += grid[y][x] - grid[y][x] // 5 * diffusion_direction_counter
    air_diffusion()

# 5. 위쪽 공기청정기의 바람은 반시계방향(RULD)으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향(RDLU)으로 순환한다.

    def air_cleaner_upper(air_cleaner_pos_x, air_cleaner_pos_y):
        x= air_cleaner_pos_x
        y= air_cleaner_pos_y
        dx_dy_list = [(0,-1),(1,0),(0,1),(-1,0)]
        air_cleaner_cache = 0
        for i in dx_dy_list:
            while True:
                air_cleaner_cache=new_grid[y][x]
                dx, dy = i
                new_x = x+dx
                new_y = y+dy
                if new_x < 0 or new_x >= x_size or new_y < 0 or new_y > air_cleaner_pos_y:
                    air_cleaner_cache=new_grid[y][x]
                    break
# 7. 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
                if new_x == air_cleaner_pos_x and new_y == air_cleaner_pos_y:
                    new_grid[air_cleaner_pos_y][air_cleaner_pos_x] = -1
                    break
                else:
# 6. 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다
                    new_grid[y][x], new_grid[new_y][new_x] = new_grid[new_y][new_x], 0
                    y += dy
                    x += dx

    air_cleaner_upper(air_cleaner[0][0], air_cleaner[0][1])

    def air_cleaner_lower(air_cleaner_pos_x, air_cleaner_pos_y):
        x= air_cleaner_pos_x
        y= air_cleaner_pos_y
        dx_dy_list = [(0,1),(1,0),(0,-1),(-1,0)]
        air_cleaner_cache = 0
        for i in dx_dy_list:
            while True:
                air_cleaner_cache=new_grid[y][x]
                dx, dy = i
                new_x = x+dx
                new_y = y+dy
                if new_x < 0 or new_x >= x_size or new_y < air_cleaner_pos_y or new_y >= y_size:
                    air_cleaner_cache=new_grid[y][x]
                    break
                if new_x == air_cleaner_pos_x and new_y == air_cleaner_pos_y:
                    new_grid[air_cleaner_pos_y][air_cleaner_pos_x] = -1
                    break
                else:
                    new_grid[y][x], new_grid[new_y][new_x] = new_grid[new_y][new_x], 0
                    y += dy
                    x += dx

    air_cleaner_lower(air_cleaner[1][0], air_cleaner[1][1])

    grid, new_grid = new_grid, [[0 for x in range(x_size)] for y in range(y_size)]

print(sum(sum(i) for i in grid)+2)