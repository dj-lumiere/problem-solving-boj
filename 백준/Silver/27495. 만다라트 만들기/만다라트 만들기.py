# B번 - 만다라트 만들기

goal_list: list[list[str]] = [list(map(str, input().split(" "))) for _ in range(9)]
offset_list: list[tuple] = [
    (0, 0),
    (1, 0),
    (2, 0),
    (2, 1),
    (2, 2),
    (1, 2),
    (0, 2),
    (0, 1),
]
main_goal_list: list[tuple] = []
main_goal_list2: list[str] = ["" for _ in range(8)]
sub_goal_list: list[list[str]] = []
sub_goal_list2: list[list[str]] = [[] for _ in range(8)]

for x in range(8):
    x_offset = 3 + offset_list[x][0]
    y_offset = 3 + offset_list[x][1]
    main_goal_list.append((goal_list[y_offset][x_offset], x))
    sub_goal_list_sub: list[str] = []
    for y in range(8):
        x_offset = offset_list[x][0] * 3 + offset_list[y][0]
        y_offset = offset_list[x][1] * 3 + offset_list[y][1]
        sub_goal_list_sub.append(goal_list[y_offset][x_offset])
    sub_goal_list_sub.sort()
    sub_goal_list.append(sub_goal_list_sub)


main_goal_list.sort()
for i, (j, k) in enumerate(main_goal_list):
    main_goal_list2[i] = j
    sub_goal_list2[i] = sub_goal_list[k]


for x in range(8):
    print(f"#{x+1}. {main_goal_list2[x]}")
    for y in range(8):
        print(f"#{x+1}-{y+1}. {sub_goal_list2[x][y]}")
