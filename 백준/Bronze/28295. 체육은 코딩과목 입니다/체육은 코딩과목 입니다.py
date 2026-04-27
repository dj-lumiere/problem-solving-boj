# 28295 체육은 코딩과목 입니다

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

rotation = 0
direction = "NESW"
for _ in range(10):
    rotation += int(input())
rotation %= 4
print(direction[rotation])