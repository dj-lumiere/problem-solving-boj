# 11549 Identifying tea

T = int(input())
print(sum(i == T for i in map(int, input().split(" "))))