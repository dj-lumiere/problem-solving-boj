# 1806 부분합

from bisect import bisect_left

N, S = list(map(int, input().split(" ")))
number_seq: list[int] = list(map(int, input().split(" ")))
accumulated_number_seq: list[int] = [0]
for i, j in enumerate(number_seq):
    accumulated_number_seq.append(j + accumulated_number_seq[-1])
possibility:bool = False
minimal_length: int = N + 1
for i, j in enumerate(accumulated_number_seq):
    if j < S:
        continue
    else:
        pointer_to_cut = bisect_left(accumulated_number_seq, j - S)
        if j - S == accumulated_number_seq[pointer_to_cut]:
            possibility = True
            minimal_length_sub: int = i - pointer_to_cut
            if minimal_length > minimal_length_sub:
                minimal_length = minimal_length_sub
        elif pointer_to_cut != 0 and j - S >= accumulated_number_seq[pointer_to_cut - 1]:
            possibility = True
            minimal_length_sub: int = i - (pointer_to_cut - 1)
            if minimal_length > minimal_length_sub:
                minimal_length = minimal_length_sub
if not possibility:
    print(0)
else:
    print(minimal_length)