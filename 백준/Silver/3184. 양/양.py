from sys import setrecursionlimit

setrecursionlimit(100000000)

y_size, x_size = list(map(int, input().split(" ")))
grid = [input() for y in range(y_size)]
grid = [[grid[y][x] for x in range(x_size)] for y in range(y_size)]
lamb_count = 0
wolf_count = 0
global lamb_count_sub, wolf_count_sub

def dfs(pos_x, pos_y):
    if pos_x < 0 or pos_x >= x_size or pos_y < 0 or pos_y >= y_size:
        return False
    if grid[pos_y][pos_x] != "#":
        if grid[pos_y][pos_x] == "o":
            global lamb_count_sub
            lamb_count_sub += 1
        elif grid[pos_y][pos_x] == "v":
            global wolf_count_sub
            wolf_count_sub += 1
        grid[pos_y][pos_x] = "#"
        dfs(pos_x + 1, pos_y)
        dfs(pos_x - 1, pos_y)
        dfs(pos_x, pos_y + 1)
        dfs(pos_x, pos_y - 1)
        return True
    else:
        return False

for x in range(x_size):
    for y in range(y_size):
        lamb_count_sub = 0
        wolf_count_sub = 0
        if dfs(x, y):
            if lamb_count_sub > wolf_count_sub:
                lamb_count += lamb_count_sub
            else:
                wolf_count += wolf_count_sub
print(lamb_count, wolf_count)