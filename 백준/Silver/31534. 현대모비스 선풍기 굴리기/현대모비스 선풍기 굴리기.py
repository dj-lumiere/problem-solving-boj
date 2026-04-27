from math import pi

a,b,h=map(int, input().split())
a,b=min(a,b),max(a,b)
print(-1 if a==b else (b**2-a**2+h**2+(2*a*h**2)/(b-a))*pi)