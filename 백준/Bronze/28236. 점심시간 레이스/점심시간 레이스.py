from sys import stdin

n, m, k = map(int, input().split(" "))
class_list = []
for i in range(1, k + 1):
    f, d = map(int, stdin.readline().strip().split(" "))
    class_list.append((f + m - d + 1, i))
class_list = sorted(class_list, key=lambda x:(x[0],x[1]))
print(class_list[0][1])