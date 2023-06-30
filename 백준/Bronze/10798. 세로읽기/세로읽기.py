# 10798 세로읽기
from itertools import zip_longest

grid = [list(input()) for _ in range(5)]

for letter_on_each_row in zip_longest(*grid, fillvalue=""):
    print(*letter_on_each_row, sep="", end="")