# 1252 이진수 덧셈

A, B = [int(i, base=2) for i in input().split(" ")]
print(bin(A + B)[2:])