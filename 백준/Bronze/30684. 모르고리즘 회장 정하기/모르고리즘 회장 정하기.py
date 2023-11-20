# 30684 모르고리즘 회장 정하기

N = int(input())
names = [input() for _ in range(N)]
filtered_names = [i for i in names if len(i) == 3]
filtered_names.sort()
print(filtered_names[0])