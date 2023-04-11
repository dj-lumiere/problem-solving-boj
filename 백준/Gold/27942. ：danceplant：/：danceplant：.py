# 27942 :danceplant:

from sys import stdin

N = int(stdin.readline().strip())
grid = [list(map(int, stdin.readline().strip().split(" "))) for _ in range(N)]
current_gaji_x_pos: int = N // 2 - 1
current_gaji_y_pos: int = N // 2 - 1
current_gaji_width: int = 2
current_gaji_height: int = 2
path = []
nutrient = 0

while True:
    left_side_nutrient = (
        sum(
            [
                grid[current_gaji_y_pos + i][current_gaji_x_pos - 1]
                for i in range(current_gaji_height)
            ]
        )
        if current_gaji_x_pos - 1 >= 0
        else -500000000
    )
    right_side_nutrient = (
        sum(
            [
                grid[current_gaji_y_pos + i][current_gaji_x_pos + current_gaji_width]
                for i in range(current_gaji_height)
            ]
        )
        if current_gaji_x_pos + current_gaji_width < N
        else -500000000
    )
    up_side_nutrient = (
        sum(
            [
                grid[current_gaji_y_pos - 1][current_gaji_x_pos + i]
                for i in range(current_gaji_width)
            ]
        )
        if current_gaji_y_pos - 1 >= 0
        else -500000000
    )
    down_side_nutrient = (
        sum(
            [
                grid[current_gaji_y_pos + current_gaji_height][current_gaji_x_pos + i]
                for i in range(current_gaji_width)
            ]
        )
        if current_gaji_y_pos + current_gaji_height < N
        else -500000000
    )
    current_max_nutrient = max(
        left_side_nutrient, right_side_nutrient, up_side_nutrient, down_side_nutrient
    )
    if (
        left_side_nutrient <= 0
        and right_side_nutrient <= 0
        and up_side_nutrient <= 0
        and down_side_nutrient <= 0
    ):
        print(nutrient)
        print(*path, sep="")
        break
    elif up_side_nutrient == current_max_nutrient:
        nutrient += current_max_nutrient
        path.append("U")
        current_gaji_height += 1
        current_gaji_y_pos -= 1
    elif down_side_nutrient == current_max_nutrient:
        nutrient += current_max_nutrient
        path.append("D")
        current_gaji_height += 1
    elif left_side_nutrient == current_max_nutrient:
        nutrient += current_max_nutrient
        path.append("L")
        current_gaji_width += 1
        current_gaji_x_pos -= 1
    elif right_side_nutrient == current_max_nutrient:
        nutrient += current_max_nutrient
        path.append("R")
        current_gaji_width += 1