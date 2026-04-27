# 30036 INK
from itertools import product

# U=(0, -1), D=(0, 1), L=(-1, 0), R=(1, 0)
# OB거나 벽과 마주치면 무시
# j는 ink += 1
# J는 잉크가 채워진 양만큼의 거리의 장애물을 칠한다. 잉크 색은 번갈아가면서 진행, 칠한 이후엔 잉크 초기화

PLAYER = "@"
WALL = "#"
DELTA = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def is_inbound(x, x_size, y, y_size):
    return 0 <= x < x_size and 0 <= y < y_size


def player_move(player_position, direction, stage_size, stage):
    x, y = player_position
    dx, dy = DELTA[direction]
    new_x, new_y = x + dx, y + dy
    if not is_inbound(new_x, stage_size, new_y, stage_size):
        return (x, y)
    if stage[new_y][new_x] == WALL:
        return (x, y)
    return (new_x, new_y)


def paint_ink(ink_color, ink_amount, player_position, stage_size, stage, result):
    player_x, player_y = player_position
    for x, y in product(range(stage_size), repeat=2):
        if abs(player_x - x) + abs(player_y - y) > ink_amount:
            continue
        if stage[y][x] != WALL:
            continue
        result[y][x] = ink_color


I, N, K = map(int, input().split(" "))
palette = list(input())
stage = [list(input()) for _ in range(N)]
commands = list(input())
result = [["." for _ in range(N)] for _ in range(N)]
player_position = (0, 0)
for i, j in product(range(N), repeat=2):
    if stage[i][j] == PLAYER:
        player_position = (j, i)
        stage[i][j] = "."
    if stage[i][j] == WALL:
        result[i][j] = WALL
ink_amount = 0
ink_color_index = 0
for command in commands:
    if command in list("UDLR"):
        player_position = player_move(player_position, command, N, stage)
    if command == "j":
        ink_amount += 1
    if command == "J":
        paint_ink(
            palette[ink_color_index], ink_amount, player_position, N, stage, result
        )
        ink_color_index = (ink_color_index + 1) % I
        ink_amount = 0
player_x, player_y = player_position
result[player_y][player_x] = PLAYER
for i in range(N):
    print(*result[i], sep="")