# 2473 세 용액

ABSOLUTE_MAX_ACIDITY = 1_000_000_000 * 3 + 1
N = int(input())
# 1. 리스트를 받아서 정리
num_list = list(map(int, input().split(" ")))
num_list.sort()
acidity = ABSOLUTE_MAX_ACIDITY
pointers = [0, 0, 0]
# 2. 포인터를 하나 고정해둬서 리스트를 한정하기
for pointer1 in range(N - 2):
    # 3. 그 한정된 리스트에서 투 포인터 쓰기
    pointer2 = pointer1 + 1
    pointer3 = N - 1
    while pointer2 < pointer3:
        acidity_sub = num_list[pointer1] + num_list[pointer2] + num_list[pointer3]
        if acidity > abs(acidity_sub):
            pointers = [pointer1, pointer2, pointer3]
            acidity = abs(acidity_sub)
        if acidity_sub == 0:
            break
        if acidity_sub > 0:
            pointer3 -= 1
        elif acidity_sub < 0:
            pointer2 += 1

print(*[num_list[i] for i in pointers])