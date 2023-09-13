# 20359 A simple task
n = int(input())
o, p = n, 0
while True:
    if o & 1:
        break
    o >>= 1
    p += 1
print(o, p)