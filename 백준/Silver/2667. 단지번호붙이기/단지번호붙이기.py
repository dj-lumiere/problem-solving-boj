# 2667 단지번호붙이기
# 땅을 리스트로 만들기
land_size = int(input())
land = []
for i in range(land_size):
    land_row = []
    land_row_str = input()
    for j in range(land_size):
        land_row.append(int(land_row_str[j]))
    land.append(land_row)

def sol():
    apt_list:list[int] = []
    apt_sub:int = 0
    # 아파트의 총합을 구함
    land_total = sum(sum(i for i in j) for j in land)
    def dfs(pos_x: int, pos_y: int):
        # 색인하려는 지역이 Out of bounds인 경우 False 반환
        if pos_x <= -1 or pos_x >= land_size or pos_y <=-1 or pos_y >= land_size:
            return False
        # 색인하려는 지역에 아파트가 있을 때
        if land[pos_y][pos_x]:
            # 중복 색인을 막기 위해 색인되었음을 표시함.
            land[pos_y][pos_x] = 0
            # 상하좌우로 색인함
            dfs(pos_x - 1, pos_y)
            dfs(pos_x + 1, pos_y)
            dfs(pos_x, pos_y - 1)
            dfs(pos_x, pos_y + 1)
            # 상하좌우로 색인을 끝내면 아파트 지역 하나가 완성되었음을 알림
            return True
        # 색인하려는 지역에 아파트가 없으면 색인 스킵
        return False
    # 아파트 지역 카운트
    apt_count = 0
    for x in range(land_size):
        for y in range(land_size):
            # 색인이 끝났으면
            if dfs(x, y):
                # 아파트 갯수에 1 더하고
                apt_count += 1
                # 지역의 아파트 갯수를 알기 위해 (색인 전 아파트 갯수) - (색인 후 아파트 갯수) 구하기
                apt_sub = land_total - sum(sum(i for i in j) for j in land)
                # 그렇게 구한 값을 아파트 갯수 리스트에 추가
                apt_list.append(apt_sub)
                # 다음 색인을 위해 아파트의 총합 다시 구하기
                land_total = sum(sum(i for i in j) for j in land)
    print(apt_count)
    apt_list.sort()
    for i in apt_list:
        print(i)

sol()
