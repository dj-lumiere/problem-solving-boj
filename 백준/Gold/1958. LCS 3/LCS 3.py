# 1953 LCS 3

A: str = input()
B: str = input()
C: str = input()
lcs_length_dp: list[list[list[int]]] = [
    [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
    for _ in range(len(C) + 1)
]

for order_a, a_letter in enumerate(A):
    for order_b, b_letter in enumerate(B):
        for order_c, c_letter in enumerate(C):
            # 문자가 같으면 길이 갱신
            if a_letter == b_letter == c_letter:
                lcs_length_dp[order_c + 1][order_b + 1][order_a + 1] = (
                    lcs_length_dp[order_c][order_b][order_a] + 1
                )
            # 문자가 다르면 A쪽에서 진행한 LCS 길이, B쪽에서 진행한 LCS의 길이, C쪽에서 진행한 LCS의 길이의 최댓값으로 갱신
            else:
                lcs_length_dp[order_c + 1][order_b + 1][order_a + 1] = max(
                    lcs_length_dp[order_c][order_b + 1][order_a + 1],
                    lcs_length_dp[order_c + 1][order_b][order_a + 1],
                    lcs_length_dp[order_c + 1][order_b + 1][order_a],
                )
print(lcs_length_dp[-1][-1][-1])