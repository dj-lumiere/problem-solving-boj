# 13711 LCS 4
from bisect import bisect_left


def find_lis_length(target: list[int]) -> int:
    from bisect import bisect_left

    target_length: int = len(target)
    sequence_indices: list[int] = [0] * (target_length + 1)
    lis_subsequence: list[int] = []
    lis_length: int = 0

    for current_index, current_value in enumerate(target):
        if not lis_subsequence or lis_subsequence[-1] < current_value:
            position = lis_length
            lis_subsequence.append(current_value)
        else:
            position = bisect_left(lis_subsequence, current_value)
        if position == lis_length:
            sequence_indices[lis_length] = current_index
            lis_subsequence[lis_length] = current_value
            lis_length += 1
        elif current_value < target[sequence_indices[position]]:
            sequence_indices[position] = current_index
            lis_subsequence[position] = current_value

    return lis_length


N: int = int(input())
A = list(map(int, input().split(" ")))
A_inv = [0] * N
for i, v in enumerate(A):
    A_inv[v - 1] = i
B = list(map(int, input().split(" ")))
B = [A_inv[v - 1] + 1 for v in B]

print(find_lis_length(B))
