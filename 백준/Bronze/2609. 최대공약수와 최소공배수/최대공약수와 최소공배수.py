X, Y = list(map(int, input().split(' ')))

def gcd(x:int, y:int) -> int:
    x, y = max(x,y), min(x,y)
    if x%y:
        return gcd(y, x%y)
    else:
        return y

def lcm(x:int, y:int) -> int:
    return x*y//gcd(x,y)

print(gcd(X, Y))
print(lcm(X, Y))