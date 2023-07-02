# 2506 점수계산

_ = int(input())
a = list(map(int, input().split()))
for index, value in enumerate(a):
    if index == 0:
        continue
    if value and a[index - 1]:
        a[index] = a[index - 1] + 1
print(sum(a))