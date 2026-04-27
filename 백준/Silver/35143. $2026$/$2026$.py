n = int(input())
if n == 1:
    print(1906)
else:
    print(1905+int("1"+"0"*(n//2-1)+"1")**2)