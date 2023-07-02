# 7567 그릇

a = list(input())
height_increment = [10]
for index, value in enumerate(a):
    if index == 0:
        continue
    if value == a[index - 1]:
        height_increment.append(5)
    else:
        height_increment.append(10)
print(sum(height_increment))