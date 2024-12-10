# 9375 패션왕 신해빈
from sys import stdin, stdout
from functools import reduce

input = stdin.readline
print = stdout.write
T = int(input())
for _ in range(T):
    N = int(input())
    if N:
        clothes_category = {}
        for _ in range(N):
            clothes_name, clothes_type = input().strip().split(" ")
            if clothes_type not in clothes_category:
                clothes_category[clothes_type] = 1
            clothes_category[clothes_type] += 1
        result = reduce(lambda x, y: x * y, clothes_category.values()) - 1
        print(f"{result}\n")
    else:
        print(f"0\n")