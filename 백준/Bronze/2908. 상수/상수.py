# 2908 상수

number_inverse = lambda x: int(str(x)[::-1])
A, B = list(map(number_inverse, input().split()))
print(max(A, B))