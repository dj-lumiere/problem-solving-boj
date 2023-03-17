# 9253 LCS 2

A = input()
B = input()
lcs_length_dp: list[list[int]] = [
    [0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)
]

for order_a, a_letter in enumerate(A):
    for order_b, b_letter in enumerate(B):
        # 문자가 같으면 길이 갱신
        if a_letter == b_letter:
            lcs_length_dp[order_b + 1][order_a + 1] = (
                lcs_length_dp[order_b][order_a] + 1
            )
        # 문자가 다르면 A쪽에서 진행한 LCS 길이와 B쪽에서 진행한 LCS의 길이의 최댓값으로 갱신
        else:
            lcs_length_dp[order_b + 1][order_a + 1] = max(
                lcs_length_dp[order_b + 1][order_a], lcs_length_dp[order_b][order_a + 1]
            )
lcs_index = lcs_length_dp[-1][-1]
lcs = ["" for _ in range(lcs_index + 1)]
i = len(A)
j = len(B)
while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
        lcs[lcs_index - 1] = A[i - 1]
        i -= 1
        j -= 1
        lcs_index -= 1
    elif lcs_length_dp[j][i - 1] > lcs_length_dp[j - 1][i]:
        i -= 1
    else:
        j -= 1
print(lcs_length_dp[-1][-1])
print(*lcs, sep="")