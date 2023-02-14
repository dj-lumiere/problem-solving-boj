# 2447 별 찍기 - 10

from sys import stdout

grid_size = int(input())
star_list = [["" for i in range(grid_size)] for j in range(grid_size)]

def mark_star(grid_size:int, row_offset:int, column_offset:int):
    if grid_size == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    star_list[column_offset+j][row_offset+i] = " "
                else:
                    star_list[column_offset+j][row_offset+i] = "*"
    else:
        row_offset -= grid_size // 3
        column_offset -= grid_size // 3
        for i in range(3):
            row_offset += grid_size // 3
            for j in range(3):
                column_offset += grid_size // 3
                if i == 1 and j == 1:
                    for x in range(grid_size // 3):
                        for y in range(grid_size // 3):
                            star_list[column_offset+y][row_offset+x]= " "
                else:
                    mark_star(grid_size//3,row_offset,column_offset)
            column_offset -= grid_size
        row_offset -= grid_size

mark_star(grid_size,0,0)

for i in star_list:
    stdout.writelines("".join(i)+"\n")
