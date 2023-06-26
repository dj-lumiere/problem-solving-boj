# 5525 IOIOI

from sys import stdin, stdout

input = stdin.readline
print = stdout.write
# OOIOIOIOIIOII
# 0123456789012
#  001122334455
#  0 1 2 3 0 0
#   0 0 0 0 1 0


N = int(input())
M = int(input())
S = list(input())
even_number_pattern = []
odd_number_pattern = []
even_number_sub = 0
odd_number_sub = 0
p_position = []
p_n_length = 2 * N + 1
result = 0
for i in range(M // 2):
    if S[2 * i : 2 * i + 2] == ["I", "O"]:
        even_number_sub += 1
    else:
        even_number_sub = 0
    if S[2 * i + 1 : 2 * i + 3] == ["I", "O"]:
        odd_number_sub += 1
    else:
        odd_number_sub = 0
    even_number_pattern.append(even_number_sub)
    odd_number_pattern.append(odd_number_sub)
even_number_pattern.append(0)
odd_number_pattern.append(0)
for index, value in enumerate(even_number_pattern):
    if index == 0:
        continue
    if even_number_pattern[index - 1] > value and value == 0:
        io_pattern_end_pos = 2 * index - 1
        p_start_sub = io_pattern_end_pos - (even_number_pattern[index - 1]) * 2 + 1
        p_end_sub = (
            io_pattern_end_pos + 1
            if S[io_pattern_end_pos + 1] == "I"
            else io_pattern_end_pos - 1
        )
        p_position.append((p_start_sub, p_end_sub))
for index, value in enumerate(odd_number_pattern):
    if index == 0:
        continue
    if odd_number_pattern[index - 1] > value and value == 0:
        io_pattern_end_pos = 2 * index
        p_start_sub = io_pattern_end_pos - (odd_number_pattern[index - 1]) * 2 + 1
        p_end_sub = (
            io_pattern_end_pos + 1
            if S[io_pattern_end_pos + 1] == "I"
            else io_pattern_end_pos - 1
        )
        p_position.append((p_start_sub, p_end_sub))
for p_start, p_end in p_position:
    p_string_length = p_end - p_start + 1
    if p_string_length >= p_n_length:
        result += (p_string_length - p_n_length) // 2 + 1
print(f"{result}")