# 27210 신을 모시는 사당

N = int(input())
orientation_list = list(map(int, input().split(" ")))
left_accumulation_sum = []
right_accumulation_sum = []
for i, j in enumerate(orientation_list):
    if i == 0:
        left_accumulation_sum.append(1 if j == 1 else 0)
        right_accumulation_sum.append(1 if j == 2 else 0)
        continue
    if j == 1:
        left_accumulation_sum.append(left_accumulation_sum[-1] + 1)
        right_accumulation_sum.append(max(0, right_accumulation_sum[-1] - 1))
    else:
        left_accumulation_sum.append(max(0, left_accumulation_sum[-1] - 1))
        right_accumulation_sum.append(right_accumulation_sum[-1] + 1)
print(max(*left_accumulation_sum, *right_accumulation_sum))