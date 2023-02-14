# 1026 보물

S = int(input())
a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))

a_list.sort()
b_list.sort(reverse=True)

print(sum(i * j for i, j in zip(a_list, b_list)))