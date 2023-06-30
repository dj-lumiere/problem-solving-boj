# 9063 대지

n = int(input())
x_pos_list = []
y_pos_list = []
for _ in range(n):
    x_pos, y_pos = map(int, input().split(" "))
    x_pos_list.append(x_pos)
    y_pos_list.append(y_pos)
print((max(x_pos_list) - min(x_pos_list)) * (max(y_pos_list) - min(y_pos_list)))