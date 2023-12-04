# 30889 좌석 배치도

N = int(input())
grid = [["." for _ in range(20)] for _ in range(10)]
for _ in range(N):
    seat = input()
    row, column = seat[0], int(seat[1:])
    row_number = ord(row) - ord("A")
    grid[row_number][column - 1] = "o"
for v in grid:
    print(*v, sep="")