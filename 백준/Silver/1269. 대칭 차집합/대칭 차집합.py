# 1269 대칭 차집합

A_size, B_size = list(map(int, input().split(" ")))
A_set = set(map(int, input().split(" ")))
B_set = set(map(int, input().split(" ")))
print(len(A_set.difference(B_set).union(B_set.difference(A_set))))