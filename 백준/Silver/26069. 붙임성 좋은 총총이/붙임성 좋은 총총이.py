# 26069 붙임성 좋은 총총이
from sys import stdin

input = stdin.readline

N = int(input())
has_met_ChongChong = set(["ChongChong"])
for _ in range(N):
    my_name, other_name = input().strip().split(" ")
    if my_name in has_met_ChongChong:
        has_met_ChongChong.add(other_name)
    elif other_name in has_met_ChongChong:
        has_met_ChongChong.add(my_name)
print(len(has_met_ChongChong))
