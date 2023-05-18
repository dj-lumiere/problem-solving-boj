# 2477 참외밭
# 반시계방향으로 점이 나열되므로, 점을 순서대로 나열한다음 신발끈 공식

K: int = int(input())
dot_list: list[tuple] = []
dot_list.append((0, 0))
for i in range(6):
    rot_dir, dist = list(map(int, input().split(" ")))
    if rot_dir == 1:
        dot_list.append((dot_list[-1][0] + dist, dot_list[-1][1]))
    elif rot_dir == 2:
        dot_list.append((dot_list[-1][0] - dist, dot_list[-1][1]))
    elif rot_dir == 3:
        dot_list.append((dot_list[-1][0], dot_list[-1][1] - dist))
    else:
        dot_list.append((dot_list[-1][0], dot_list[-1][1] + dist))
area: int = 0
for i in range(6):
    area += (
        dot_list[i][0] * dot_list[i + 1][1] - dot_list[-i - 1][0] * dot_list[-i - 2][1]
    )
print(area * K // 2)