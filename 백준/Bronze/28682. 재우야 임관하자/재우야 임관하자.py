# 28682 재우야 임관하자

A, B, C = "swimming", "bowling", "soccer"
n = int(input())
print(*([A] * 1500), sep=" ", flush=True)
failed_list = input().split(" ")
probable_list = []
for i in failed_list:
    if i == B:
        probable_list.append(C)
    else:
        probable_list.append(B)
print(*probable_list, flush=True)