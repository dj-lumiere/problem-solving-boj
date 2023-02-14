import sys

sys.setrecursionlimit(10**7)

# 2583 영역 구하기
# 땅을 리스트로 만들기
y_size, x_size, fill_land = list(map(int, input().split(" ")))
land = [[0 for x in range(x_size)] for y in range(y_size)]
for i in range(fill_land):
    x1, y1, x2, y2 = list(map(int, input().split(" ")))
    for x in range(x1, x2):
        for y in range(y_size-y2, y_size-y1):
            land[y][x] = 1

def sol():
    land_list:list[int] = []
    land_sub:int = 0
    # 채워진 칸의 총합을 구함
    land_total = sum(sum(i for i in j) for j in land)
    def dfs(pos_x: int, pos_y: int):
        # 색인하려는 지역이 Out of bounds인 경우 False 반환
        if pos_x <= -1 or pos_x >= x_size or pos_y <=-1 or pos_y >= y_size:
            return False
        # 색인하려는 지역에 채워진 칸가 있을 때
        if not land[pos_y][pos_x]:
            # 중복 색인을 막기 위해 색인되었음을 표시함.
            land[pos_y][pos_x] = 1
            # 상하좌우로 색인함
            dfs(pos_x - 1, pos_y)
            dfs(pos_x + 1, pos_y)
            dfs(pos_x, pos_y - 1)
            dfs(pos_x, pos_y + 1)
            # 상하좌우로 색인을 끝내면 채워진 칸 지역 하나가 완성되었음을 알림
            return True
        # 색인하려는 지역에 채워진 칸가 없으면 색인 스킵
        return False
    # 채워진 칸 지역 카운트
    land_count = 0
    for x in range(x_size):
        for y in range(y_size):
            # 색인이 끝났으면
            if dfs(x, y):
                # 채워진 칸 갯수에 1 더하고
                land_count += 1
                # 지역의 채워진 칸 갯수를 알기 위해 (색인 후 채워진 칸 갯수) - (색인 전 채워진 칸 갯수) 구하기
                land_sub = sum(sum(i for i in j) for j in land) - land_total
                # 그렇게 구한 값을 채워진 칸 갯수 리스트에 추가
                land_list.append(land_sub)
                # 다음 색인을 위해 채워진 칸의 총합 다시 구하기
                land_total = sum(sum(i for i in j) for j in land)
    print(land_count)
    land_list.sort()
    for i in land_list:
        print(i, end=" ")

sol()
