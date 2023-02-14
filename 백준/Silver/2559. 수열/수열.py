# 2559 수열

N, k = list(map(int, input().split(" ")))
temp_list = list(map(int, input().split(" ")))
temp_diff = sum(temp_list[0:k])
temp_diff_max = temp_diff
for i in range(N - k):
    temp_diff = temp_diff + temp_list[i+k] - temp_list[i]
    if temp_diff_max < temp_diff:
        temp_diff_max = temp_diff
print(temp_diff_max)