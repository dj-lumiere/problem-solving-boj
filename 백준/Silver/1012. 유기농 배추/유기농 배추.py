from sys import stdin, setrecursionlimit

setrecursionlimit(2500000)

test_cases = int(input())

for i in range(test_cases):

    grid_width, grid_height, cabbage_count = list(map(int, input().split(" ")))

    # 배추밭 현황을 2차원 리스트로 만든다
    def cabbage_gridify(grid_width: int, grid_height: int, cabbage_count: int) -> list[list[int]]:
        cabbage_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]
        for i in range(cabbage_count):
            pos = stdin.readline().rstrip()
            pos_x, pos_y = list(map(int, pos.split(" ")))
            cabbage_grid[pos_y][pos_x] = 1
        return cabbage_grid

    cabbage_grid = cabbage_gridify(grid_width, grid_height, cabbage_count)

    # DFS
    def dfs(pos_x, pos_y):
        if pos_x <= -1 or pos_x >= grid_width or pos_y <=-1 or pos_y >= grid_height:
            return False
        if cabbage_grid[pos_y][pos_x]:
            cabbage_grid[pos_y][pos_x] = 0
            dfs(pos_x - 1, pos_y)
            dfs(pos_x + 1, pos_y)
            dfs(pos_x, pos_y - 1)
            dfs(pos_x, pos_y + 1)
            return True
        return False

    result = 0
    for x in range(grid_width):
        for y in range(grid_height):
            if dfs(x, y):
                result += 1

    print(result)
