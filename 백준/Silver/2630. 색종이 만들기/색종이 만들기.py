from sys import stdin
from math import log

initial_grid_size = int(input())
initial_color_grid = []
for i in range(initial_grid_size):
    initial_color_grid.append(list(map(int, stdin.readline().rstrip().split(" "))))

color_paper_count = {"blue":0, "white":0}

def color_paper(grid_size:int, color_grid: list[list[int]], x_start:int, y_start:int, color_paper_count:dict[str, int]) -> dict[str, int]:
    x_finish = x_start + grid_size
    y_finish = y_start + grid_size
    blue_count = 0
    white_count = 0
    for i in range(x_start, x_finish):
        for j in range(y_start, y_finish):
            if color_grid[j][i] == 1:
                blue_count += 1
            else:
                white_count += 1
    if blue_count == (grid_size)**2:
        color_paper_count["blue"] += 1
    elif white_count == (grid_size)**2:
        color_paper_count["white"] += 1
    else:
        for i in range(2):
            for j in range(2):
                color_paper(grid_size//2, color_grid, x_start+((grid_size//2)*i), y_start+((grid_size//2)*j), color_paper_count)
    return color_paper_count

color_paper_result = color_paper(initial_grid_size, initial_color_grid, 0, 0, color_paper_count)

print(f'{color_paper_result["white"]}\n{color_paper_result["blue"]}')