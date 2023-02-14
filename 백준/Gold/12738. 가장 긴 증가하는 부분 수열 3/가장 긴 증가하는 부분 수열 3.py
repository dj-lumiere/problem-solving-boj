# 12738 가장 긴 증가하는 부분 수열 3

N = int(input())
A = list(map(int, input().split(" ")))

tails = [0] * N
size = 0
path = []
for i, j in enumerate(A):
    x, y = 0, size
    while x != y:
        m = (x+y)//2
        if tails[m] < j:
            x = m+1
        else:
            y = m
    tails[x] = j
    size = max(x+1, size)
print(size)