# 21736 헌내기는 친구가 필요해

from itertools import product

# I의 위치 찾기
# DFS로 벽과 OB로 이루어진 덩어리를 하나 찾기
# 거기에 사람이 몇 있는지 확인하기

grid_height, grid_width = map(int, input().strip().split(" "))
grid = [list(input().strip()) for i in range(grid_height)]
starting_point = [0, 0]
for y, x in product(range(grid_height), range(grid_width)):
    if grid[y][x] == "I":
        starting_point = [x, y]
        break


delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dfs_stack = [(starting_point[0], starting_point[1])]
answer = 0


def is_inbounds(pos_x: int, pos_y: int, grid_width: int, grid_height: int):
    return 0 <= pos_x < grid_width and 0 <= pos_y < grid_height


while dfs_stack:
    current_x, current_y = dfs_stack.pop()
    for dx, dy in delta:
        next_x, next_y = current_x + dx, current_y + dy
        if not is_inbounds(next_x, next_y, grid_width, grid_height):
            continue
        if grid[next_y][next_x] == "X":
            continue
        if grid[next_y][next_x] == "P":
            answer += 1
        dfs_stack.append((next_x, next_y))
        grid[next_y][next_x] = "X"
print(f'{answer if answer else "TT"}')
