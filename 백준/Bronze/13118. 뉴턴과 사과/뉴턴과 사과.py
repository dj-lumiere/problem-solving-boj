# 13118 뉴턴과 사과

p = map(int, input().split(" "))
x, _, r = map(int, input().split(" "))
collsion = [i for i, v in enumerate(p, start=1) if abs(v - x) == 0]
if not collsion:
    collsion.append(0)
print(*collsion)