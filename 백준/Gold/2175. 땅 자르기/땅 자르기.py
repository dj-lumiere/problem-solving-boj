# 2175 땅 자르기
# 좌표 4개와 중점 구하기 시계방향이니 걱정할 필요는 없음
point_list = list(map(int, input().split(" ")))
xy_coordinate = [(point_list[2*i],point_list[2*i+1]) for i in range(4)]
mid_point = [((xy_coordinate[i%4][0]+xy_coordinate[(i+1)%4][0])/2,(xy_coordinate[i%4][1]+xy_coordinate[(i+1)%4][1])/2) for i in range(4)]

final_coordinate = []
for i in range(4):
    final_coordinate.append(xy_coordinate[i])
    final_coordinate.append(mid_point[i])

# 8개의 점 중에 자를 구간을 찾아 넓이 구하기 (신발끈 공식 이용)

# 이 리스트는 같은 선에 있는 경우를 모아둔 것이므로 제외
exclude_list = [(i%8,(i+1)%8) for i in range(8)]+[(i%8,(i+1)%8) for i in range(0,8,2)]

# 자를 두 점의 번호를 구하기
def permut(N:int, M:int) -> list[list[int]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            element = []
            for i in stack:
                element.append(i)
            if element not in exclude_list:
                list_permut.append(element)
            return
        else:
            for i in range(init, N):
                if i not in stack:
                    stack.append(i)
                    dfs(i+1, M-1, stack)
                    stack.pop()
    dfs(0, M, stack)
    return list_permut

permut_list:list[list[int]] = permut(8,2)
split_polygon_point_list = []
# 잘린 두 점에 대해서 그 두 점을 포함하는 꼭짓점들을 전부 집어넣기
for i in permut_list:
    split_polygon_point_list.append([final_coordinate[i[0]]]+[final_coordinate[j] for j in range(i[0]+1, i[1]) if j%2 == 0]+[final_coordinate[i[1]]])

# 다각형의 넓이의 차가 제일 작은 것을 출력한다
area_difference = 10**25
final_polygon_area = 0
rectangle_area = 1/2 * abs(sum(xy_coordinate[i%4][0]*xy_coordinate[(i+1)%4][1]-xy_coordinate[i%4][1]*xy_coordinate[(i+1)%4][0] for i in range(4)))
polygon_area_dict = dict()
for i in split_polygon_point_list:
    polygon_area = 1/2 * abs(sum(i[j%len(i)][0]*i[(j+1)%len(i)][1]-i[j%len(i)][1]*i[(j+1)%len(i)][0] for j in range(len(i))))
    if area_difference > abs(rectangle_area-polygon_area*2):
        area_difference = min(area_difference, abs(rectangle_area-polygon_area*2))
        final_polygon_area = polygon_area

final_polygon_area = min(final_polygon_area, rectangle_area - final_polygon_area)
print(final_polygon_area, rectangle_area - final_polygon_area)
