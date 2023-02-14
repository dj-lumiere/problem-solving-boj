from sys import stdin
from math import log

initial_grid_size = int(input())
initial_number_grid = []
for i in range(initial_grid_size):
    initial_number_grid.append(list(map(int, stdin.readline().rstrip().split(" "))))

number_paper_count = {"plus_1":0, "zero":0, "minus_1":0}

def number_paper(grid_size:int, number_grid: list[list[int]], x_start:int, y_start:int, number_paper_count:dict[str, int]) -> dict[str, int]:
    x_finish = x_start + grid_size
    y_finish = y_start + grid_size
    plus_1_count = 0
    zero_count = 0
    minus_1_count = 0
    for i in range(x_start, x_finish):
        for j in range(y_start, y_finish):
            if number_grid[j][i] == 1:
                plus_1_count += 1
            elif number_grid[j][i] == -1:
                minus_1_count += 1
            else:
                zero_count +=1
    if plus_1_count == (grid_size)**2:
        number_paper_count["plus_1"] += 1
    elif zero_count == (grid_size)**2:
        number_paper_count["zero"] += 1
    elif minus_1_count == (grid_size)**2:
        number_paper_count["minus_1"] += 1
    else:
        for i in range(3):
            for j in range(3):
                number_paper(grid_size//3, number_grid, x_start+((grid_size//3)*i), y_start+((grid_size//3)*j), number_paper_count)
    return number_paper_count

number_paper_result = number_paper(initial_grid_size, initial_number_grid, 0, 0, number_paper_count)

print(f'{number_paper_result["minus_1"]}\n{number_paper_result["zero"]}\n{number_paper_result["plus_1"]}')