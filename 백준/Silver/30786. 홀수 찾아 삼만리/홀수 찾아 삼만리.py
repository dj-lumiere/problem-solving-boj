# A번 - 홀수 찾아 삼만리
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
points = []
oddity = []
for _ in range(N):
    x, y = map(int, input().split(" "))
    points.append((x, y))
    oddity.append((x + y) & 1)
if all(not i for i in oddity) or all(i for i in oddity):
    print("NO")
else:
    print("YES")
    start = oddity.index(0)
    end = oddity.index(1)
    answer = [start + 1]
    for i in range(N):
        if i in (start, end):
            continue
        answer.append(i + 1)
    answer.append(end + 1)
    print(*answer)