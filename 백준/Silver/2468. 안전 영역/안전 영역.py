import sys
sys.setrecursionlimit(10**7)

land_size = int(input())
land = []
for i in range(land_size):
    land.append(list(map(int, input().split(" "))))

land_max = max(max(i) for i in land)
safe_zone_dict = {i:0 for i in range(1,land_max+1)}
for i in range(1, land_max+1):
    safe_land = [[(land[y][x]>=i) for x in range(land_size)] for y in range(land_size)]
    def dfs(pos_x:int, pos_y:int):
        if pos_x <= -1 or pos_x >= land_size or pos_y <= -1 or pos_y >= land_size:
            return 0
        else:
            if safe_land[pos_y][pos_x]:
                safe_land[pos_y][pos_x] = False
                dfs(pos_x+1, pos_y)
                dfs(pos_x-1, pos_y)
                dfs(pos_x, pos_y+1)
                dfs(pos_x, pos_y-1)
                return 1
        return 0
    for x in range(land_size):
        for y in range(land_size):
            safe_zone_dict[i] += dfs(x,y)
print(max(safe_zone_dict[i] for i in range(1, land_max+1)))