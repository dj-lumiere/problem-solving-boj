# 13532 악마의 수열

from decimal import Decimal, getcontext

getcontext().prec = 31000

x = (Decimal(2)/Decimal(3))*(1-Decimal("-0.5")**int(input()))
x_tuple = x.as_tuple()[1]
for (i, j) in enumerate(x_tuple):
    if i == 0 and j != 6:
        print(0)
    elif x_tuple[i-1] == 6 and j != 6:
        print(i)
        break