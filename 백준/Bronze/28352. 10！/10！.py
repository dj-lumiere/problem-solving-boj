from math import factorial

ONE_WEEK = 7 * 24 * 60 * 60
N = int(input())
print(factorial(N)//ONE_WEEK)