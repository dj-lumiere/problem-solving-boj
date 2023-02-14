height_list = []

for i in range(9):
    height_list.append(int(input()))

def sol(height_list: list[int]) -> list[int]:
    height_sum = sum(height_list)
    height_goal = height_sum - 100
    for i in range(9):
        for j in range(i):
            if height_list[i]+height_list[j] == height_goal:
                height_list.pop(i)
                height_list.pop(j)
                height_list.sort()
                return(height_list)
                break
            else:
                continue

final_list = sol(height_list)[:]
for i in range(7):
    print(final_list[i])
