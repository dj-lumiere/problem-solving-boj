# 15712 등비수열

a, r, n, m = list(map(int, input().split(" ")))
if r == 1:
    x = a * n
    print(x % m)
else:
    x = a * (pow(r, n, m * (r - 1)) - 1)
    print(x // (r - 1) % m)