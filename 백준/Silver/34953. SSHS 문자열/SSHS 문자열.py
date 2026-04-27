n = int(input())
if n < 4:
    print("S"*n)
elif n % 3 == 1:
    print("SSH"*(n//3)+"S")
elif n % 3 == 2:
    print("SSH"*(n//3)+"SS")
else:
    print("S"+"SSH"*(n//3-1)+"SS")