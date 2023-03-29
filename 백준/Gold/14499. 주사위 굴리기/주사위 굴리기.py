# 14499 주사위 굴리기

N, M, pos_y, pos_x, K = list(map(int, input().split(" ")))
score_grid: list[list[int]] = [list(map(int, input().split(" "))) for _ in range(N)]
command_list: list[int] = list(map(int, input().split(" ")))
# UDLRFB
dice_value = [0, 0, 0, 0, 0, 0]


def spin_east():
    # DLUR -> LURD
    (dice_value[2], dice_value[0], dice_value[3], dice_value[1],) = (
        dice_value[1],
        dice_value[2],
        dice_value[0],
        dice_value[3],
    )


def spin_west():
    # DLUR -> RDLU
    (dice_value[3], dice_value[1], dice_value[2], dice_value[0],) = (
        dice_value[1],
        dice_value[2],
        dice_value[0],
        dice_value[3],
    )


def spin_north():
    # BUFD -> DBUF
    (dice_value[1], dice_value[5], dice_value[0], dice_value[4],) = (
        dice_value[5],
        dice_value[0],
        dice_value[4],
        dice_value[1],
    )


def spin_south():
    # BUFD -> UFDB
    (dice_value[0], dice_value[4], dice_value[1], dice_value[5],) = (
        dice_value[5],
        dice_value[0],
        dice_value[4],
        dice_value[1],
    )


def dice_movement(pos_x: int, pos_y: int):
    if score_grid[pos_y][pos_x] == 0:
        score_grid[pos_y][pos_x] = dice_value[1]
    else:
        dice_value[1] = score_grid[pos_y][pos_x]
        score_grid[pos_y][pos_x] = 0
    print(dice_value[0])


for j in command_list:
    if j == 1 and pos_x + 1 < M:
        pos_x += 1
        spin_east()
        dice_movement(pos_x, pos_y)
    elif j == 2 and pos_x - 1 >= 0:
        pos_x -= 1
        spin_west()
        dice_movement(pos_x, pos_y)
    elif j == 3 and pos_y - 1 >= 0:
        pos_y -= 1
        spin_north()
        dice_movement(pos_x, pos_y)
    elif j == 4 and pos_y + 1 < N:
        pos_y += 1
        spin_south()
        dice_movement(pos_x, pos_y)