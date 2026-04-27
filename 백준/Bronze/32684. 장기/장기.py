s = (13,7,5,3,3,2)
a = sum(x*y for x, y in zip(map(int, input().split()), s))
b = sum(x*y for x, y in zip(map(int, input().split()), s))+1.5
if a>b: print("cocjr0208")
else: print("ekwoo")