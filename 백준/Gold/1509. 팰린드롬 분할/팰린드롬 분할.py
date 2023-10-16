# 1509 팰린드롬 분할

# 일단 펠린드롬인 구간을 전부 다 구하기
A = input()
# is_palindromic[i][j] = A[i..j]의 palindrome 여부
is_palindromic = [[False for _ in range(len(A))] for i in range(len(A))]
for x in range(len(A)):
    for y in range(len(A) - x):
        i, j = y, y + x
        if i + 1 > j - 1:
            is_palindromic[i][j] = A[i] == A[j]
            continue
        is_palindromic[i][j] = A[i] == A[j] and is_palindromic[i + 1][j - 1]

# min_partition_count[i] = i번째 자리까지의 파티션 개수의 최솟값
min_partition_count = [0 for _ in range(len(A))]
min_partition_count[0] = 1
for i in range(1, len(A)):
    sub_counts = [min_partition_count[i - 1] + 1]
    for j in range(i):
        if is_palindromic[j][i]:
            sub_counts.append((min_partition_count[j - 1] if j >= 1 else 0) + 1)
    min_partition_count[i] = min(sub_counts)
print(min_partition_count[-1])