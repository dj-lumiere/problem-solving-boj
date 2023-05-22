# C번 - 동전 복사

N = int(input())
x, y = [int(i) for i in input().split(" ")]

# 이미 전체가 다 차있으면 0칸
if N == x == y == 1:
    print(0)
# 꼭지점이면 2회
elif (x, y) in [(1, 1), (1, N), (N, 1), (N, N)]:
    print(2)
# 변이면 3회
elif x in (1, N) or y in (1, N):
    print(3)
# 사각형 안쪽이면 4회
else:
    print(4)