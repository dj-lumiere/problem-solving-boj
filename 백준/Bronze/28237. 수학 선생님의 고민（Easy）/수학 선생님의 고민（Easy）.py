from fractions import Fraction

n = int(input())
D = 5*n**2+10*n+1
if int(D**0.5)**2 != D:
    print(-1)
else:
    root_1 = Fraction(-(n+1)+int(D**.5),2*n)
    root_2 = Fraction(-(n+1)-int(D**.5),2*n)
    a, b = root_1.denominator, -root_1.numerator
    c, d = root_2.denominator, -root_2.numerator
    print(a, b, c, d)