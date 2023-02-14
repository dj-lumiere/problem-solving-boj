# 1850 최대공약수

def gcd(x, y):
    if x < y:
        x, y = y, x
    if x % y:
        return gcd(x%y, y)
    else:
        return y
A, B = list(map(int, input().split(" ")))
print("1"*gcd(A, B))