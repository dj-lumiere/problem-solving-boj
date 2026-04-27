# 30642 아이그루스와 화장실

N = int(input())
name = input()
K = int(input())
if name == "annyong":
    if K & 1:
        print(K)
    else:
        print(K - 1 if K > 1 else K + 1)
else:
    if K & 1:
        print(K - 1 if K > 1 else K + 1)
    else:
        print(K)