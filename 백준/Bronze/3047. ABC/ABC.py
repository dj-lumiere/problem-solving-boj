# 3047 ABC

x, y, z = map(int, input().split(" "))
print_order = list(input())
number = {chr(ord("A") + i): v for i, v in enumerate(sorted([x, y, z]))}
print(*[number[i] for i in print_order])