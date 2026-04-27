from itertools import product
n = int(input())
a = range(2, 10)
b = range(1, 10)
c = map(lambda x: x[0]*x[1], product(a, b))
print(++(n in set(a).union(set(b)).union(set(c))))