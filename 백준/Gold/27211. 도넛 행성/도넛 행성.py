# 27211 도넛 행성

# -1, x_size는 OOB가 아니라 N-1, 0이 됨.
# 나머지는 땅덩어리 구하는 DFS 뭐시깽이 문제들과 비슷함

from sys import setrecursionlimit

setrecursionlimit(10**7*4)


y_size, x_size = list(map(int, input().split(" ")))

forest_grid = [list(map(int, input().split(" "))) for i in range(y_size)]

# DFS
def dfs(pos_x, pos_y):
    if forest_grid[pos_y][pos_x] == 0:
        forest_grid[pos_y][pos_x] = 1
        dfs((pos_x - 1) % x_size, pos_y)
        dfs((pos_x + 1) % x_size, pos_y)
        dfs(pos_x, (pos_y - 1) % y_size)
        dfs(pos_x, (pos_y + 1) % y_size)
        return True
    return False


result = 0
for x in range(x_size):
    for y in range(y_size):
        if dfs(x, y):
            result += 1

print(result)