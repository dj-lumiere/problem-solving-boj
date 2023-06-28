# 17256 달달함이 넘쳐흘러

ax, ay, az = map(int, input().split(" "))
cx, cy, cz = map(int, input().split(" "))
# az+bx=cx, ay*by=cy, ax+bz=cz
bx, by, bz = cx - az, cy // ay, cz - ax
print(bx, by, bz)