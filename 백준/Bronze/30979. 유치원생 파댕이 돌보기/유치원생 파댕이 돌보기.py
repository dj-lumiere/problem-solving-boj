# 30979 유치원생 파댕이 돌보기

T = int(input())
N = int(input())
F = list(map(int, input().split(" ")))
print(f"Padaeng_i {'Cry' if sum(F) < T else 'Happy'}")