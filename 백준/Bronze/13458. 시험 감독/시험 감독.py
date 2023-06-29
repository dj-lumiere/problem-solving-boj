# 13458 시험 감독
from math import ceil

N = int(input())
A = list(map(int, input().split(" ")))
B, C = map(int, input().split(" "))
print(sum([1 + max(0, ceil((i - B) / C)) for i in A]))