#2436 공약수

g, l = list(map(int, input().split(" ")))

#lcm//gcd 구하기
a_b = l // g

addition = 2*10**8
a, b = [0,0]

def gcd(x:int, y:int) -> int:
    x, y = max(x,y), min(x,y)
    if x%y:
        return gcd(y, x%y)
    else:
        return y
#약수쌍 중에 둘의 차이를 최소화하는 쌍을 구하기
for i in range(1, int(a_b**.5)+1):
    if a_b % i == 0:
        a_sub = i
        b_sub = a_b // i
        if a_sub + b_sub < addition and gcd(a_sub, b_sub) == 1:
            addition = a_sub*g + b_sub*g
            a, b = [a_sub*g, b_sub*g]
print(a,b)
