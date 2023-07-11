# 2473 세 용액

N = int(input())
# 1. 리스트를 받아서 정리
num_list = list(map(int, input().split(" ")))
num_list.sort()
neutrality = 3000000000
ptr = [0,0,0]
# 2. 포인터를 하나 고정해둬서 리스트를 한정하기
for ptr_i in range(N-2):
    # 3. 그 한정된 리스트에서 투 포인터 쓰기
    ptr_j = ptr_i+1
    ptr_k = N-1
    while ptr_j < ptr_k:
        neutrality_sub = num_list[ptr_i]+num_list[ptr_j]+num_list[ptr_k]
        if neutrality > abs(neutrality_sub):
            ptr = [ptr_i, ptr_j, ptr_k]
            neutrality = abs(neutrality_sub)
        if neutrality_sub > 0:
            ptr_k -= 1
        else:
            ptr_j += 1

print(" ".join(map(str, list(num_list[i] for i in ptr))))
