# 31218 자료 구조의 왕

from sys import stdin


def input():
    return stdin.readline().strip()


def is_inbound(pos_x, x_size, pos_y, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


def query_1(dx, dy, start_x, start_y):
    global grass_count
    stack = [(start_x - 1, start_y - 1)]
    while stack:
        x, y = stack.pop()
        if not grid[y][x]:
            break
        grid[y][x] = 0
        grass_count -= 1
        if not is_inbound(x + dx, m, y + dy, n):
            break
        stack.append((x + dx, y + dy))


def query_2(x, y):
    return grid[y - 1][x - 1]


n, m, q = map(int, input().split())
grid = [[1 for _ in range(m)] for _ in range(n)]
grass_count = n * m
for _ in range(q):
    opcode, *operand = map(int, input().split())
    if opcode == 1:
        query_1(*operand)
    if opcode == 2:
        print(1 - query_2(*operand))
    if opcode == 3:
        print(grass_count)