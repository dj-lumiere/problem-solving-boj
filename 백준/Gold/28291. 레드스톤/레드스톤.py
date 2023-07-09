# 28291 레드스톤
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
from collections import deque

NON_CONDUCTIVE = -1
CONDUCTIVE = 0
REDSTONE_BLOCK_POWER = 16
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_inbound(pos_x: int, pos_y: int, x_size: int, y_size: int) -> bool:
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


def int_if_available(target: str) -> int | str:
    try:
        return int(target)
    except:
        return target


x_size, y_size = map(int, input().split(" "))
redstone_power_intensity = [
    [NON_CONDUCTIVE for _ in range(x_size)] for _ in range(y_size)
]
block_type_grid = [["" for _ in range(x_size)] for _ in range(y_size)]
visited = [[False for _ in range(x_size)] for _ in range(y_size)]
lamp_position = []
curcuit_bfs_queue = deque()
block_count = int(input())

for _ in range(block_count):
    block_type, block_pos_x, block_pos_y = map(int_if_available, input().split(" "))
    if block_type == "redstone_dust":
        block_type_grid[block_pos_y][block_pos_x] = "dust"
        redstone_power_intensity[block_pos_y][block_pos_x] = CONDUCTIVE
    if block_type == "redstone_block":
        block_type_grid[block_pos_y][block_pos_x] = "block"
        redstone_power_intensity[block_pos_y][block_pos_x] = REDSTONE_BLOCK_POWER
        visited[block_pos_y][block_pos_x] = True
        curcuit_bfs_queue.append((block_pos_x, block_pos_y))
    if block_type == "redstone_lamp":
        block_type_grid[block_pos_y][block_pos_x] = "lamp"
        redstone_power_intensity[block_pos_y][block_pos_x] = CONDUCTIVE
        lamp_position.append((block_pos_x, block_pos_y))


while curcuit_bfs_queue:
    current_x_pos, current_y_pos = curcuit_bfs_queue.popleft()
    if block_type_grid[current_y_pos][current_x_pos] == "lamp":
        continue
    for delta_x, delta_y in DELTA:
        next_x_pos, next_y_pos = current_x_pos + delta_x, current_y_pos + delta_y
        if not is_inbound(next_x_pos, next_y_pos, x_size, y_size):
            continue
        if not block_type_grid[next_y_pos][next_x_pos]:
            continue
        if redstone_power_intensity[current_y_pos][current_x_pos] < 1:
            continue
        if visited[next_y_pos][next_x_pos]:
            continue
        redstone_power_intensity[next_y_pos][next_x_pos] = (
            redstone_power_intensity[current_y_pos][current_x_pos] - 1
        )
        visited[next_y_pos][next_x_pos] = True
        curcuit_bfs_queue.append((next_x_pos, next_y_pos))

if all([redstone_power_intensity[y][x] > 0 for x, y in lamp_position]):
    print("success")
else:
    print("failed")