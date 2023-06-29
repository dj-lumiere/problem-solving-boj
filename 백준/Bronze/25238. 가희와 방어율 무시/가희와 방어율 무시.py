# 25238 가희와 방어율 무시
i, j = map(int, input().split(" "))
print(int(i * (100 - j) < 10000))