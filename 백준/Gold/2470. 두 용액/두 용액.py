# 2470 두 용액

N = int(input())
# 1. 리스트를 받아서 정리
num_list = list(map(int, input().split(" ")))
num_list.sort()
neutrality = 2000000000
ptr = [0, 0]
# 2. 투 포인터
ptr_i = 0
ptr_j = N - 1
while ptr_i < ptr_j:
    neutrality_sub = num_list[ptr_i] + num_list[ptr_j]
    if neutrality > abs(neutrality_sub):
        ptr = [ptr_i, ptr_j]
        neutrality = abs(neutrality_sub)
    if neutrality_sub > 0:
        ptr_j -= 1
    else:
        ptr_i += 1

print(" ".join(map(str, list(num_list[i] for i in ptr))))
