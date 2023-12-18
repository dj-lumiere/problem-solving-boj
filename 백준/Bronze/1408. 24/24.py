# 1408 24

a, b, c = map(int, input().split(":"))
d, e, f = map(int, input().split(":"))
d += 24
s = ((d - a) * 60 + (e - b)) * 60 + (f - c)
m, s = divmod(s, 60)
h, m = divmod(m, 60)
_, h = divmod(h, 24)
print(f"{h:0>2}:{m:0>2}:{s:0>2}")