# 24313 알고리즘 수업 - 점근적 표기 1

a1, a0 = map(int, input().split(" "))
c = int(input())
n0 = int(input())
print(int((c - a1 >= 0 and (c - a1) * n0 - a0 >= 0)))