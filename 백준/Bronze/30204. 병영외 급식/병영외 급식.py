N, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
print(1-int(bool(sum(A)%X)))