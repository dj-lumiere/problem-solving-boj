# 1297 TV 크기
from math import sqrt

D, H, W = map(int, input().split(" "))
print(int(D * H / sqrt(H**2 + W**2)), int(D * W / sqrt(H**2 + W**2)))