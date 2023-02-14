# 2635 수 이어가기

N = int(input())
maximum_length = 2
max_number_sequence = []
for i in range(N, 1 - 1, -1):
    number_sequence = [N, i]
    ptr_i, ptr_j = 0, 1
    while True:
        next_node = number_sequence[ptr_i] - number_sequence[ptr_j]
        if next_node >= 0:
            number_sequence.append(next_node)
            ptr_i += 1
            ptr_j += 1
        else:
            if len(number_sequence) > maximum_length:
                maximum_length = len(number_sequence)
                max_number_sequence = number_sequence[:]
            break
    if maximum_length == 2:
        max_number_sequence = number_sequence[:]
print(maximum_length)
print(" ".join(map(str, max_number_sequence)))