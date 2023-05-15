# 2892 심심한 준규

message_length = int(input())
encrypted_message = [int(f"0x{value}", base=0) for value in input().split()]
is_alphabet_lower_case = []
a = ord("a")
z = ord("z")
zero = ord("0")
for value in encrypted_message:
    is_alphabet_lower_case_indicator = False
    for test_keys in range(9 + 1):
        if a <= (test_keys + zero) ^ value <= z:
            is_alphabet_lower_case_indicator = True
            break
    if is_alphabet_lower_case_indicator:
        is_alphabet_lower_case.append("-")
    else:
        is_alphabet_lower_case.append(".")
print(*is_alphabet_lower_case, sep="")