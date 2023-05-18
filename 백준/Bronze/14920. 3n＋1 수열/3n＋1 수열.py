# 14920 3n+1 수열

c: int = int(input())
n: int = 1
while c != 1:
    n += 1
    if c & 1:
        c = 3 * c + 1
    else:
        c >>= 1
print(n)