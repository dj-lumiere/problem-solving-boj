# 10026 적록색약

from sys import setrecursionlimit

# 재귀 제한 해제
setrecursionlimit(10000000)

# R, G, B에 대해 그래프화
image_size:int = int(input())
image:list[list[str]] = []
for y in range(image_size):
    image_row:list[str] = []
    image_row_str:str = input()
    for x in range(image_size):
        image_row.append(image_row_str[x])
    image.append(image_row)

# R에 대해 그래프화
r_image:list[list[bool]] = [[False for x in range(image_size)] for y in range(image_size)]
for x in range(image_size):
    for y in range(image_size):
        r_image[y][x] = (image[y][x] == "R")

# G에 대해 그래프화
g_image:list[list[bool]] = [[False for x in range(image_size)] for y in range(image_size)]
for x in range(image_size):
    for y in range(image_size):
        g_image[y][x] = (image[y][x] == "G")

# R+G에 대해 그래프화
rg_image:list[list[bool]] = [[False for x in range(image_size)] for y in range(image_size)]
for x in range(image_size):
    for y in range(image_size):
        rg_image[y][x] = r_image[y][x] | g_image[y][x]

# B에 대해 그래프화
b_image:list[list[bool]] = [[False for x in range(image_size)] for y in range(image_size)]
for x in range(image_size):
    for y in range(image_size):
        b_image[y][x] = (image[y][x] == "B")

#dfs 기본 로직
def dfs(graph, pos_x, pos_y):
    if pos_x < 0 or pos_x >= image_size or pos_y < 0 or pos_y >= image_size:
        return False
    if graph[pos_y][pos_x]:
        graph[pos_y][pos_x] = False
        dfs(graph, pos_x - 1, pos_y)
        dfs(graph, pos_x + 1, pos_y)
        dfs(graph, pos_x, pos_y - 1)
        dfs(graph, pos_x, pos_y + 1)
        return True
    return False

r_object, g_object, rg_object, b_object = [0,0,0,0]

for x in range(image_size):
    for y in range(image_size):
        # R에 대해 dfs
        if dfs(r_image, x, y):
            r_object += 1
        # R+G에 대해 dfs
        if dfs(rg_image, x, y):
            rg_object += 1
        # G에 대해 dfs
        if dfs(g_image, x, y):
            g_object += 1
        # B에 대해 dfs
        if dfs(b_image, x, y):
            b_object += 1

print(r_object+g_object+b_object, end=" ")
print(rg_object+b_object)