from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(90000)
y_size, x_size = list(map(int, input().split(" ")))
graph: list[list[int]] = [
    list(map(int, stdin.readline().rstrip().split(" "))) for y in range(y_size)
]
graph2: list[list[int]] = [[0 for x in range(x_size)] for y in range(y_size)]
T: int = 0
dx_dy_list: list[tuple] = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_inbound(pos_x, x_size, pos_y, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


def dfs(start_x, start_y):
    stack = [(start_x, start_y)]
    count = 0

    while stack:
        pos_x, pos_y = stack.pop()
        if is_inbound(pos_x, x_size, pos_y, y_size) and graph[pos_y][pos_x] != 0:
            graph[pos_y][pos_x] = 0
            count += 1
            stack.append((pos_x - 1, pos_y))
            stack.append((pos_x + 1, pos_y))
            stack.append((pos_x, pos_y - 1))
            stack.append((pos_x, pos_y + 1))

    return 1 if count > 0 else 0


# 얼음 녹이기
def ice_melting():
    while bfs_queue:
        x, y = bfs_queue.popleft()
        melting_direction_counter: int = 0
        for dx, dy in dx_dy_list:
            nx: int = x + dx
            ny: int = y + dy
            if 0 <= nx < x_size and 0 <= ny < y_size and graph2[ny][nx] == 0:
                melting_direction_counter += 1
            graph[y][x] = max(graph2[y][x] - melting_direction_counter, 0)


while True:
    graph2 = [[graph[y][x] for x in range(x_size)] for y in range(y_size)]
    icebergs: int = 0
    dfs_stack: list = []
    bfs_queue: deque = deque()
    for x in range(x_size):
        for y in range(y_size):
            if graph[y][x] > 0:
                dfs_stack.append((x, y))
                bfs_queue.append((x, y))
    # 얼음 덩어리 갯수 구하기
    for x, y in dfs_stack:
        icebergs += dfs(x, y)
    dfs_stack.clear()
    if icebergs > 1:
        break
    elif not bfs_queue:
        T = 0
        break
    else:
        ice_melting()
        graph2 = [[graph[y][x] for x in range(x_size)] for y in range(y_size)]
        T += 1
        bfs_queue.clear()
print(T)