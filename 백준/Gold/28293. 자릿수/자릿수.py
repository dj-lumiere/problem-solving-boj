# 28293 자릿수

from decimal import Decimal, getcontext

getcontext().prec = 30
a, b = map(Decimal, input().split(" "))
a = a.log10()
a *= b
print(int(a.__ceil__()))