# 보드게임컵 A번 - 노 땡스!

N = int(input())
x = list(map(int, input().split(" ")))
x2 = x[:]

score = 0
for i, j in enumerate(x):
    if i > 0:
        if j - 1 == x[i - 1]:
            x2[i] = 0
print(sum(x2))