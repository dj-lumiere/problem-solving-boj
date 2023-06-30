# 2010 플러그
from sys import stdin

input = stdin.readline
N = int(input())
answer = 0
for _ in range(N):
    capacity = int(input())
    answer += capacity - 1
answer += 1
print(answer)