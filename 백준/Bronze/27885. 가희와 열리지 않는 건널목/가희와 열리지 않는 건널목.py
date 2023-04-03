# B번 - 가희와 열리지 않는 건널목

baricade_check: list[bool] = [True for _ in range(24 * 60 * 60)]

c, h = list(map(int, input().split(" ")))
for _ in range(c + h):
    hh, mm, ss = list(map(int, input().split(":")))
    t = (hh * 60 + mm) * 60 + ss
    baricade_check[t : t + 40] = [False] * 40
print(sum(baricade_check))