# 2166 다각형의 면적
N: int = int(input())
x_coord_list: list[int] = []
y_coord_list: list[int] = []
for _ in range(N):
    x_coord_sub, y_coord_sub = list(map(int, input().split(" ")))
    x_coord_list.append(x_coord_sub)
    y_coord_list.append(y_coord_sub)
x_coord_list.append(x_coord_list[0])
y_coord_list.append(y_coord_list[0])

answer: int = 0
for i in range(N):
    answer = (
        answer
        + x_coord_list[i] * y_coord_list[i + 1]
        - x_coord_list[-i - 1] * y_coord_list[-i - 2]
    )
print(abs(answer/2))