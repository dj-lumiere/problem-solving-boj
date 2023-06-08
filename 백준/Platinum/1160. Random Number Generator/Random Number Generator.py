# 1160 Random Number Generator

m, a, c, x0, n, g = map(int, input().split(" "))
result = 0
if a == 0:
    result = c % m
if a == 1:
    result = (x0 + c * n) % m
else:
    result = (
        (((a - 1) * x0 + c) * pow(a, n, m * (a - 1)) - c) % (m * (a - 1)) // (a - 1)
    )
print(result % g)
