# 10867 중복 빼고 정렬하기

_ = int(input())
print(*sorted(set(map(int, input().split()))))