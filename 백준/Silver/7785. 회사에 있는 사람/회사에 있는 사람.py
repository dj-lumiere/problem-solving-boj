# 7785 회사에 있는 사람
from sys import stdin

input = stdin.readline

in_workplace = set()
n = int(input())
for _ in range(n):
    name, act = input().strip().split(" ")
    if act == "enter":
        in_workplace.add(name)
    elif act == "leave" and name in in_workplace:
        in_workplace.remove(name)
in_workplace_as_list = list(in_workplace)
in_workplace_as_list.sort()
in_workplace_as_list.reverse()
print(*in_workplace_as_list, sep="\n")
