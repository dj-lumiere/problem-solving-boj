import math

a, b = list(map(int,input().split(" ")))
c, d = list(map(int,input().split(" ")))

def quotient_sum(a:int,b:int,c:int,d:int):
    lcm_nom = math.lcm(b,d)
    sum_denom = a*lcm_nom//b+c*lcm_nom//d
    sum_denom, lcm_nom = sum_denom // math.gcd(sum_denom, lcm_nom), lcm_nom // math.gcd(sum_denom, lcm_nom)
    print(f"{sum_denom} {lcm_nom}")

def gcd(x:int, y:int) -> int:
    if not x%y:
        return gcd(y, x%y)
    else:
        return y

def lcm(x:int, y:int) -> int:
    return x*y//gcd(x,y)

quotient_sum(a,b,c,d)