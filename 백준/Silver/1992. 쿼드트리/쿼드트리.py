from sys import stdin
from math import log

initial_grid_size = int(input())
initial_color_grid = []

for i in range(initial_grid_size):
    row = stdin.readline().rstrip()
    row_list = [int(row[i]) for i in range(initial_grid_size)]
    initial_color_grid.append(row_list)

quad_tree_list = []

def quad_tree(grid_size:int, color_grid: list[list[int]], x_start:int, y_start:int, quad_tree_list:list[str]):
    x_finish = x_start + grid_size
    y_finish = y_start + grid_size
    black_count = 0
    white_count = 0
    for i in range(x_start, x_finish):
        for j in range(y_start, y_finish):
            if color_grid[j][i] == 1:
                black_count += 1
            else:
                white_count += 1

    if black_count == (grid_size)**2:
        quad_tree_list.append("1")
    elif white_count == (grid_size)**2:
        quad_tree_list.append("0")

    else:
        quad_tree_list_sub = []
        for j in range(2):
            for i in range(2):
                quad_tree(grid_size//2, color_grid, x_start+((grid_size//2)*i), y_start+((grid_size//2)*j), quad_tree_list_sub)
        quad_tree_list.append("("+"".join(quad_tree_list_sub)+")")

quad_tree(initial_grid_size, initial_color_grid, 0, 0, quad_tree_list)

print(quad_tree_list[0])