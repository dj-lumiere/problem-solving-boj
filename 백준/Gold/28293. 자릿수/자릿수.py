# 28293 자릿수

from decimal import Decimal, getcontext

getcontext().prec = 60
a, b = map(Decimal, input().split(" "))
a = a.log10()
a *= b
print(int(a.__floor__()) + 1)
