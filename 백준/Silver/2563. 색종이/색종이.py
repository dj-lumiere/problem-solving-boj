# 2563 색종이

grid = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
for _ in range(N):
    paper_x_start, paper_y_start = map(int, input().split(" "))
    for i in range(10):
        grid[paper_y_start + i][paper_x_start : paper_x_start + 10] = [1] * 10
print(sum([sum(i) for i in grid]))