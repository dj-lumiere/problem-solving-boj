N = int(input())
A = list(map(int, input().split(" ")))

dict_A = dict()
for i, a in enumerate(A):
    dict_A[a] = i

M = int(input())
F = list(map(int, input().split(" ")))

for target in F:
    if target in dict_A:
        print(1)
    else:
        print(0)